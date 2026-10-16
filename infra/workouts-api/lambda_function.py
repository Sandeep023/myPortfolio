"""Workout profiles API for sandeepindukuri.com/workouts.

Lambda function URL (CORS handled by the URL config). Routes:
  GET    /profiles                      list profiles
  POST   /profiles                      {name, pin}        create profile (admin PIN)
  POST   /admin/check                   {pin}              verify admin PIN
  POST   /admin/pin                     {pin, newPin}      change admin PIN
  GET    /p/{id}                        {state, history}
  PUT    /p/{id}/state                  {state}
  PATCH  /p/{id}/state                  {set, del}         merge changed keys; returns merged state
  POST   /p/{id}/history                {session}
  DELETE /p/{id}/history/{sid}
  POST   /p/{id}/import                 {state, history}   replace a profile's data (restore)
  GET    /photos                                           {exerciseId: version} for every exercise photo
  GET    /photo/{exerciseId}                               the image (cache forever; URL carries ?v=version)
  POST   /photo/{exerciseId}            {pin, data, type}  add/replace a photo (admin PIN, base64 JPEG/PNG/WebP)
  POST   /photo/{exerciseId}/delete     {pin}              remove a photo (admin PIN)
Profiles are never deleted through the API.
"""
import base64, hashlib, hmac, json, os, re, secrets, time
import boto3
from boto3.dynamodb.conditions import Key

TABLE = boto3.resource("dynamodb").Table(os.environ["TABLE"])
S3 = boto3.client("s3")
BUCKET = os.environ.get("BUCKET", "")
MAX_PHOTO = 2_500_000
IMG_TYPES = {"image/jpeg": b"\xff\xd8\xff", "image/png": b"\x89PNG", "image/webp": b"RIFF"}
ID_RE = re.compile(r"^[a-z0-9-]{1,48}$")
SID_RE = re.compile(r"^[A-Za-z0-9_-]{1,48}$")
MAX_STATE, MAX_SESSION, MAX_IMPORT = 120_000, 30_000, 380_000
LOCK_AFTER, LOCK_SECS = 5, 900


def resp(code, body):
    return {"statusCode": code, "headers": {"content-type": "application/json", "cache-control": "no-store"}, "body": json.dumps(body)}


def body_of(event):
    raw = event.get("body") or ""
    if event.get("isBase64Encoded"):
        raw = base64.b64decode(raw).decode()
    if len(raw) > max(MAX_IMPORT, MAX_PHOTO * 4 // 3) + 4000:
        raise ValueError("Request is too large.")
    return json.loads(raw) if raw else {}


def pin_hash(pin, salt):
    return hashlib.pbkdf2_hmac("sha256", pin.encode(), bytes.fromhex(salt), 200_000).hex()


def check_admin(pin):
    """Returns None if OK, else an error response. Locks for 15 min after 5 bad tries."""
    now = int(time.time())
    lock = TABLE.get_item(Key={"pk": "ADMIN", "sk": "LOCK"}).get("Item") or {}
    if int(lock.get("until", 0)) > now:
        return resp(429, {"error": "Too many wrong PINs. Try again in %d minutes." % ((int(lock["until"]) - now) // 60 + 1)})
    rec = TABLE.get_item(Key={"pk": "ADMIN", "sk": "PIN"}).get("Item")
    if rec and isinstance(pin, str) and 4 <= len(pin) <= 64 and hmac.compare_digest(pin_hash(pin, rec["salt"]), rec["hash"]):
        if lock.get("fails"):
            TABLE.put_item(Item={"pk": "ADMIN", "sk": "LOCK", "fails": 0, "until": 0})
        return None
    fails = int(lock.get("fails", 0)) + 1
    TABLE.put_item(Item={"pk": "ADMIN", "sk": "LOCK", "fails": 0 if fails >= LOCK_AFTER else fails,
                         "until": now + LOCK_SECS if fails >= LOCK_AFTER else 0})
    return resp(403, {"error": "That admin PIN is wrong."})


def list_profiles():
    items = TABLE.query(KeyConditionExpression=Key("pk").eq("PROFILES"))["Items"]
    out = [{"id": i["sk"][2:], "name": i["name"], "createdAt": i.get("createdAt")} for i in items]
    out.sort(key=lambda p: (p["id"] != "sandeep", p.get("createdAt") or ""))
    return out


def profile_exists(pid):
    return ID_RE.match(pid) and "Item" in TABLE.get_item(Key={"pk": "PROFILES", "sk": "P#" + pid})


def get_profile_data(pid):
    items, kw = [], {"KeyConditionExpression": Key("pk").eq("P#" + pid)}
    while True:
        r = TABLE.query(**kw)
        items += r["Items"]
        if "LastEvaluatedKey" not in r:
            break
        kw["ExclusiveStartKey"] = r["LastEvaluatedKey"]
    state, hist = {}, []
    for i in items:
        if i["sk"] == "STATE":
            state = json.loads(i["data"])
            state.pop("_v", None)
        elif i["sk"].startswith("H#"):
            hist.append(json.loads(i["data"]))
    hist.sort(key=lambda s: s.get("dateISO", ""))
    return {"state": state, "history": hist}


def clean_session(s):
    if not isinstance(s, dict) or not SID_RE.match(str(s.get("id", ""))):
        raise ValueError("Session needs a valid id.")
    if len(json.dumps(s)) > MAX_SESSION:
        raise ValueError("Session is too large.")
    return s


def handler(event, context):
    method = event.get("requestContext", {}).get("http", {}).get("method", "GET")
    path = (event.get("rawPath") or "/").rstrip("/") or "/"
    parts = [p for p in path.split("/") if p]
    try:
        if parts == ["profiles"] and method == "GET":
            return resp(200, {"profiles": list_profiles()})

        if parts == ["profiles"] and method == "POST":
            b = body_of(event)
            err = check_admin(b.get("pin"))
            if err:
                return err
            name = " ".join(str(b.get("name", "")).split())[:40]
            if not name:
                return resp(400, {"error": "Enter a name for the profile."})
            if any(p["name"].lower() == name.lower() for p in list_profiles()):
                return resp(409, {"error": "A profile called %s already exists." % name})
            pid = (re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")[:36] or "p") + "-" + secrets.token_hex(2)
            item = {"pk": "PROFILES", "sk": "P#" + pid, "name": name, "createdAt": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
            TABLE.put_item(Item=item, ConditionExpression="attribute_not_exists(sk)")
            return resp(201, {"profile": {"id": pid, "name": name, "createdAt": item["createdAt"]}})

        if parts == ["photos"] and method == "GET":
            items = TABLE.query(KeyConditionExpression=Key("pk").eq("PHOTOS"))["Items"]
            return resp(200, {"photos": {i["sk"]: int(i["ver"]) for i in items}})

        if len(parts) >= 2 and parts[0] == "photo" and ID_RE.match(parts[1]):
            ex = parts[1]
            key = "photos/" + ex
            if len(parts) == 2 and method == "GET":
                try:
                    o = S3.get_object(Bucket=BUCKET, Key=key)
                except S3.exceptions.NoSuchKey:
                    return resp(404, {"error": "No photo for this exercise."})
                return {"statusCode": 200, "isBase64Encoded": True, "body": base64.b64encode(o["Body"].read()).decode(),
                        "headers": {"content-type": o.get("ContentType", "image/jpeg"), "cache-control": "public, max-age=31536000, immutable"}}
            if len(parts) == 2 and method == "POST":
                b = body_of(event)
                err = check_admin(b.get("pin"))
                if err:
                    return err
                ctype = str(b.get("type", "image/jpeg"))
                if ctype not in IMG_TYPES:
                    return resp(400, {"error": "Use a JPEG, PNG or WebP photo."})
                try:
                    data = base64.b64decode(str(b.get("data", "")), validate=True)
                except Exception:
                    return resp(400, {"error": "That photo couldn't be read."})
                if not data.startswith(IMG_TYPES[ctype]) or len(data) > MAX_PHOTO:
                    return resp(400, {"error": "That photo is too large or not an image."})
                S3.put_object(Bucket=BUCKET, Key=key, Body=data, ContentType=ctype)
                ver = int(time.time() * 1000)
                TABLE.put_item(Item={"pk": "PHOTOS", "sk": ex, "ver": ver})
                return resp(200, {"ok": True, "ver": ver})
            if parts[2:] == ["delete"] and method == "POST":
                err = check_admin(body_of(event).get("pin"))
                if err:
                    return err
                S3.delete_object(Bucket=BUCKET, Key=key)
                TABLE.delete_item(Key={"pk": "PHOTOS", "sk": ex})
                return resp(200, {"ok": True})

        if parts == ["admin", "check"] and method == "POST":
            err = check_admin(body_of(event).get("pin"))
            return err or resp(200, {"ok": True})

        if parts == ["admin", "pin"] and method == "POST":
            b = body_of(event)
            err = check_admin(b.get("pin"))
            if err:
                return err
            new = str(b.get("newPin", ""))
            if not (6 <= len(new) <= 64):
                return resp(400, {"error": "The new PIN needs at least 6 characters."})
            salt = secrets.token_hex(16)
            TABLE.put_item(Item={"pk": "ADMIN", "sk": "PIN", "salt": salt, "hash": pin_hash(new, salt)})
            return resp(200, {"ok": True})

        if len(parts) >= 2 and parts[0] == "p":
            pid = parts[1]
            if not profile_exists(pid):
                return resp(404, {"error": "No profile with that id."})
            if len(parts) == 2 and method == "GET":
                return resp(200, get_profile_data(pid))
            if parts[2:] == ["state"] and method == "PUT":
                st = body_of(event).get("state")
                data = json.dumps(st if isinstance(st, dict) else {})
                if len(data) > MAX_STATE:
                    return resp(413, {"error": "Saved progress is too large."})
                TABLE.put_item(Item={"pk": "P#" + pid, "sk": "STATE", "data": data, "updatedAt": int(time.time())})
                return resp(200, {"ok": True})
            if parts[2:] == ["state"] and method == "PATCH":
                b = body_of(event)
                sets = b.get("set") if isinstance(b.get("set"), dict) else {}
                dels = [str(k) for k in (b.get("del") or [])][:2000]
                for _ in range(6):  # optimistic concurrency: retry if another device saved in between
                    cur = TABLE.get_item(Key={"pk": "P#" + pid, "sk": "STATE"}, ConsistentRead=True).get("Item")
                    st = json.loads(cur["data"]) if cur else {}
                    ver = int(cur.get("ver", 0)) if cur else 0
                    st.pop("_v", None)
                    st.update(sets)
                    for k in dels:
                        st.pop(k, None)
                    data = json.dumps(st)
                    if len(data) > MAX_STATE:
                        return resp(413, {"error": "Saved progress is too large."})
                    try:
                        TABLE.put_item(Item={"pk": "P#" + pid, "sk": "STATE", "data": data, "ver": ver + 1, "updatedAt": int(time.time())},
                                       ConditionExpression="attribute_not_exists(sk) OR attribute_not_exists(ver) OR ver = :v",
                                       ExpressionAttributeValues={":v": ver})
                        return resp(200, {"state": st})
                    except TABLE.meta.client.exceptions.ConditionalCheckFailedException:
                        continue
                return resp(409, {"error": "Busy saving, try again."})
            if parts[2:] == ["history"] and method == "POST":
                s = clean_session(body_of(event).get("session"))
                TABLE.put_item(Item={"pk": "P#" + pid, "sk": "H#" + s["id"], "data": json.dumps(s)})
                return resp(201, {"ok": True})
            if len(parts) == 4 and parts[2] == "history" and method == "DELETE" and SID_RE.match(parts[3]):
                TABLE.delete_item(Key={"pk": "P#" + pid, "sk": "H#" + parts[3]})
                return resp(200, {"ok": True})
            if parts[2:] == ["import"] and method == "POST":
                b = body_of(event)
                st = b.get("state") if isinstance(b.get("state"), dict) else {}
                hist = [clean_session(s) for s in (b.get("history") or [])][:2000]
                old = TABLE.query(KeyConditionExpression=Key("pk").eq("P#" + pid) & Key("sk").begins_with("H#"), ProjectionExpression="pk, sk")["Items"]
                with TABLE.batch_writer() as w:
                    for o in old:
                        w.delete_item(Key={"pk": o["pk"], "sk": o["sk"]})
                    w.put_item(Item={"pk": "P#" + pid, "sk": "STATE", "data": json.dumps(st), "updatedAt": int(time.time())})
                    for s in hist:
                        w.put_item(Item={"pk": "P#" + pid, "sk": "H#" + s["id"], "data": json.dumps(s)})
                return resp(200, {"ok": True, "sessions": len(hist)})
        return resp(404, {"error": "Not found."})
    except (ValueError, json.JSONDecodeError) as e:
        return resp(400, {"error": str(e) or "Bad request."})
