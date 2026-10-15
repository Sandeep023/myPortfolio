"""Source of truth for the 5-day plan. Generates plan.js (embedded in the app) and report tables."""
import json

def ex(id, name, primary, region, secondary, equipment, kind, sets, reps, rest, tempo, steps, variants, notes=""):
    return dict(id=id, name=name, primary=primary, tgt=region, secondary=secondary, equipment=equipment, kind=kind,
                sets=str(sets), reps=reps, rest=rest, tempo=tempo, steps=steps, variants=variants, alts=notes)

V = lambda label, video=None, anim=None, src=None: dict(label=label, video=video, anim=anim, src=src)

PLAN = [
 dict(day="Monday", abbr="MON", focus="Shoulders + Forearms + Traps", duration="65–80",
  tip="Press first while your shoulders are fresh, then isolate each delt head. Shrugs and forearm work go last so grip fatigue doesn't limit the shoulder work. Leave 1–3 reps in reserve; add weight once you hit the top of the rep range on every set with clean form.",
  muscles=[
   dict(name="Shoulders", cls="m1", ex=[
    ex("seated-db-press","Seated Dumbbell Shoulder Press","Deltoids","Front and side delts","Triceps, upper chest","Dumbbells, upright bench","Compound",3,"8–10","120s","3-1-1",
       ["Set the bench upright and start with the dumbbells just above shoulder height.","Brace your core and keep your back on the pad.","Press up and slightly in until your arms are nearly straight.","Lower under control to ear level; don't let the elbows flare behind you."],
       [V(None,"dumbbell-seated-shoulders-press","ohp_front","Dumbbell/Shoulders/Dumbbell Seated Shoulders Press.mp4")]),
    ex("cable-lateral-raise","Cable Lateral Raise","Deltoids","Side (lateral) delts","Upper traps, supraspinatus","Cable, single handle","Isolation",3,"12–15","75s","2-1-2",
       ["Stand side-on to a low pulley and lean slightly away holding the post.","Raise the far arm out to the side with a soft elbow.","Stop at shoulder height; lead with the elbow, not the hand.","Lower slowly, keeping tension on the cable. Do every rep, then switch sides."],
       [V(None,"cable-leaning-lateral-raise","lateral_raise","Cable Machine/Shoulders/Cable Leaning Lateral Raise.mp4")]),
    ex("seated-db-reverse-fly","Seated Dumbbell Reverse Fly","Deltoids","Rear (posterior) delts","Rhomboids, middle traps","Dumbbells, bench","Isolation",3,"12–15","75s","2-1-2",
       ["Sit on the end of a bench and hinge forward until your chest nears your thighs.","Let the dumbbells hang under your shoulders, palms facing in.","Raise them out wide with slightly bent elbows; squeeze the backs of your shoulders.","Lower slowly. Keep your neck neutral and don't swing."],
       [V(None,"dumbbell-seated-reverse-fly","rear_fly_top","Dumbbell/Back/Dumbbell Seated Reverse Fly.mp4")],
       "Stands in for the reverse pec deck: your pack has no reverse pec deck clip."),
    ex("db-front-raise","Dumbbell Front Raise","Deltoids","Front (anterior) delts","Upper chest","Dumbbells","Isolation",2,"10–12","60s","2-1-2",
       ["Stand tall with the dumbbells in front of your thighs.","Raise one or both arms forward to shoulder height, elbows soft.","Pause briefly; don't lean back to lift the weight.","Lower under control."],
       [V(None,"dumbbell-standing-front-raise","front_raise","Dumbbell/Shoulders/Dumbbell Standing Front Raise.mp4")],
       "Optional: the press already trains the front delts. Skip it if your shoulders feel beaten up."),
   ]),
   dict(name="Trapezius", cls="m2", ex=[
    ex("db-shrug","Dumbbell Shrug","Trapezius","Upper traps","Levator scapulae, grip","Dumbbells","Isolation",3,"10–15","75s","1-2-1",
       ["Stand tall with heavy dumbbells at your sides.","Lift your shoulders straight up toward your ears.","Hold the top for a second; don't roll the shoulders.","Lower all the way for a full stretch."],
       [V(None,"dumbbell-shrug","shrug_db","Dumbbell/Back/Dumbbell Shrug.mp4")]),
   ]),
   dict(name="Forearms", cls="m2", ex=[
    ex("seated-wrist-curl","Seated Wrist Curl","Forearms","Wrist flexors (inner forearm)","Grip","Barbell or dumbbells, bench","Isolation",2,"15–20","60s","2-1-2",
       ["Sit with your forearms on your thighs, palms facing up, wrists past your knees.","Let the bar roll down to your fingertips.","Curl your wrists up as high as they go; squeeze.","Lower slowly. Your forearms stay on your thighs."],
       [V(None,"barbell-seated-wrist-curl","wrist_curl","Barbell/Arm/Barbell Seated Wrist Curl.mp4")]),
    ex("reverse-wrist-curl","Reverse Wrist Curl","Forearms","Wrist extensors (outer forearm)","Brachioradialis","Barbell or dumbbells, bench","Isolation",2,"15–20","60s","2-1-2",
       ["Same setup as the wrist curl, but palms facing down.","Let your hands drop toward the floor.","Lift the backs of your hands up as high as you can.","Use a light weight; lower slowly."],
       [V(None,None,"reverse_wrist_curl")],
       "Video not available: your pack has no reverse wrist curl. The drawing shows the movement."),
    ex("reverse-curl","Reverse-Grip Curl","Forearms","Brachioradialis and wrist extensors","Brachialis, biceps","Cable straight bar (or EZ bar)","Isolation",2,"10–12","60s","2-1-2",
       ["Hold the bar overhand, hands shoulder-width.","Keep your elbows pinned at your sides.","Curl up until your forearms are vertical, wrists straight.","Lower slowly to full extension."],
       [V(None,"cable-reverse-grip-bicep-curl","reverse_curl","Cable Machine/Bicep/Cable Reverse Grip Bicep Curl.mp4")],
       "The video shows the cable version; an EZ bar works the same way."),
   ]),
  ]),
 dict(day="Tuesday", abbr="TUE", focus="Legs + Glutes + Calves", duration="80–100",
  tip="Squat and hinge first while you're fresh, then the machines, then the small muscles. Do 1–2 lighter ramp-up sets before squats and RDLs. Keep 2 reps in reserve on squats and RDLs so your lower back recovers for Thursday.",
  muscles=[
   dict(name="Quads + Glutes", cls="m1", ex=[
    ex("back-squat","Barbell Back Squat","Quadriceps","All four quad heads","Glutes, adductors, spinal erectors","Barbell, squat rack","Compound",3,"6–10","180s","3-1-1",
       ["Bar on your upper traps, feet shoulder-width, toes turned out slightly.","Brace your core hard before every rep.","Sit down and back; knees track over your toes.","Drive up through the whole foot, hips and chest rising together."],
       [V(None,"barbell-back-squat","squat","Barbell/Legs/Barbell Back Squat.mp4")]),
    ex("leg-extension","Leg Extension","Quadriceps","Rectus femoris, vastus medialis","—","Leg extension machine","Isolation",2,"12–15","75s","2-1-2",
       ["Line your knees up with the machine's pivot and set the pad on your lower shins.","Grip the handles and sit back.","Straighten your legs fully and squeeze your quads for a second.","Lower slowly; don't let the stack slam."],
       [V(None,"lever-leg-extension","leg_extension","Gym Machine/Legs/Lever Leg Extension.mp4")]),
   ]),
   dict(name="Hamstrings + Glutes", cls="m1", ex=[
    ex("rdl","Romanian Deadlift","Hamstrings","Biceps femoris, semitendinosus, semimembranosus","Glutes, spinal erectors","Barbell","Compound",3,"8–10","150s","3-1-1",
       ["Stand tall with the bar at your thighs, knees slightly bent.","Push your hips back, sliding the bar down your legs.","Stop when your hamstrings are fully stretched, back flat.","Drive your hips forward to stand up."],
       [V(None,"barbell-romanian-deadlift","rdl","Barbell/Legs/Barbell Romanian Deadlift.mp4")]),
    ex("hip-thrust","Barbell Hip Thrust","Glutes","Gluteus maximus","Hamstrings","Barbell, bench, bar pad","Compound",2,"8–12","120s","2-2-1",
       ["Upper back on the bench edge, bar padded across your hips.","Feet flat, about hip-width, shins vertical at the top.","Drive through your heels until your hips are level with your shoulders.","Squeeze your glutes for two seconds, then lower."],
       [V(None,"barbell-hip-thrust",None,"Barbell/Legs/Barbell Hip Thrust.mp4")]),
    ex("lying-leg-curl","Lying Leg Curl","Hamstrings","Knee flexion (all three hamstrings)","Calves","Lying leg curl machine","Isolation",3,"10–15","75s","2-1-3",
       ["Lie face down with the pad just above your heels.","Keep your hips pressed into the bench.","Curl your heels toward your glutes.","Lower slowly over three seconds."],
       [V(None,"lever-lying-leg-curl","lying_leg_curl","Gym Machine/Legs/Lever Lying Leg Curl.mp4")],
       "Stands in for the seated leg curl: your pack only has the lying version."),
   ]),
   dict(name="Hips", cls="m2", ex=[
    ex("cable-hip-abduction","Cable Hip Abduction","Glutes","Gluteus medius and minimus","Tensor fasciae latae","Cable ankle strap","Isolation",2,"12–15","60s","2-1-2",
       ["Strap the cuff on your outside ankle and stand side-on to a low pulley.","Hold the post and stand tall.","Sweep the leg out to the side without leaning.","Return slowly. Do all reps, then switch legs."],
       [V(None,"cable-hip-abduction",None,"Cable Machine/Legs/Cable Hip Abduction.mp4")],
       "Stands in for the hip abductor machine. Use the machine if your gym has one."),
    ex("hip-adduction","Hip Adductor Machine","Adductors","Inner thighs","—","Hip adductor machine","Isolation",2,"12–15","60s","2-1-2",
       ["Sit with the pads on the inside of your knees.","Start with your legs as wide as is comfortable.","Squeeze your knees together.","Open slowly under control."],
       [V(None,None,"hip_adduction")],
       "Video not available: your pack has no adduction exercise. The drawing shows the movement."),
   ]),
   dict(name="Calves + Shins", cls="m2", ex=[
    ex("standing-calf-raise","Standing Calf Raise","Calves","Gastrocnemius","Soleus","Smith machine (or calf machine), step","Isolation",3,"12–15","60s","1-2-1",
       ["Stand with the balls of your feet on a raised edge.","Keep your knees straight but not locked.","Rise as high as you can and pause.","Lower until your heels are below the edge for a full stretch."],
       [V(None,"smith-standing-calf-raise","calf_raise","Smith Machine/Legs/Smith Standing Calf Raise.mp4")]),
    ex("seated-calf-raise","Seated Calf Raise","Calves","Soleus","Gastrocnemius","Seated calf machine","Isolation",2,"15–20","60s","1-2-1",
       ["Sit with the pad on your lower thighs and the balls of your feet on the plate.","Release the safety and let your heels drop.","Push up onto your toes and hold for a second.","Lower slowly for a deep stretch."],
       [V(None,"lever-seated-calf-raise",None,"Gym Machine/Legs/Lever Seated Calf Raise.mp4")]),
    ex("tibialis-raise","Tibialis Raise","Tibialis anterior","Front of the shin","—","Wall (or tib bar)","Isolation",2,"15–20","45s","1-1-1",
       ["Lean your back against a wall with your heels about a foot out.","Keep your legs straight.","Pull your toes up toward your shins as far as you can.","Lower slowly without letting your toes slap down."],
       [V(None,None,"tib_raise")],
       "Video not available: your pack has no tibialis exercise. The drawing shows the movement."),
   ]),
  ]),
 dict(day="Wednesday", abbr="WED", focus="Chest + Triceps", duration="65–80",
  tip="Incline first so your upper chest gets your best effort, then flat and decline. Triceps go last because every press has already worked them. Do 1–2 ramp-up sets before the first press.",
  muscles=[
   dict(name="Chest", cls="m1", ex=[
    ex("incline-db-press","Incline Dumbbell Press","Chest","Upper chest (clavicular head)","Front delts, triceps","Dumbbells, incline bench","Compound",3,"8–10","120s","3-1-1",
       ["Set the bench to 30–45°. Start with the dumbbells over your upper chest.","Pinch your shoulder blades back and down.","Lower until the dumbbells are beside your upper chest, elbows about 45–60° from your body.","Press up and slightly in; stop just short of locking out."],
       [V(None,"dumbbell-incline-bench-press","incline_db_press","Dumbbell/Chest/Dumbbell Incline Bench Press.mp4")]),
    ex("flat-bb-bench","Flat Barbell Bench Press","Chest","Mid chest (sternal head)","Front delts, triceps","Barbell, flat bench","Compound",3,"6–10","180s","3-1-1",
       ["Eyes under the bar, feet planted, shoulder blades pinched.","Grip slightly wider than shoulders.","Lower the bar to your mid chest, elbows tucked about 45–75°.","Press back up over your shoulders. Use a spotter or safeties."],
       [V(None,"barbell-bench-press","flat_bb_press","Barbell/Chest/Barbell Bench Press.mp4")]),
    ex("decline-machine-press","Decline Machine Chest Press","Chest","Lower chest (lower sternal fibres)","Triceps","Decline press machine","Compound",2,"10–12","90s","2-1-1",
       ["Adjust the seat so the handles line up with your lower chest.","Keep your back on the pad and chest up.","Press forward and down until your arms are almost straight.","Return slowly until you feel a stretch."],
       [V(None,"lever-decline-chest-press","decline_press","Gym Machine/Chest/Lever Decline Chest Press.mp4")]),
    ex("cable-fly-high-low","High-to-Low Cable Fly","Chest","Lower chest emphasis","Front delts","Cable crossover, high pulleys","Isolation",2,"12–15","75s","2-1-2",
       ["Set both pulleys high and step forward into a split stance.","Start with your arms wide, elbows soft.","Sweep your hands down and together in front of your hips.","Squeeze, then let your arms open slowly."],
       [V(None,"cable-chest-fly","fly_top","Cable Machine/Chest/Cable Chest Fly.mp4")]),
   ]),
   dict(name="Triceps", cls="m2", ex=[
    ex("overhead-cable-ext","Overhead Cable Triceps Extension","Triceps","Long head","Medial and lateral heads","Cable, rope","Isolation",3,"10–15","75s","3-1-1",
       ["Face away from the pulley with the rope behind your head.","Keep your elbows pointing forward and close to your head.","Extend your arms fully overhead.","Lower slowly until you feel a deep stretch in the backs of your arms."],
       [V(None,"cable-seated-overhead-tricep-extension","overhead_ext","Cable Machine/Tricep/Cable Seated Overhead Tricep Extension.mp4")]),
    ex("rope-pushdown","Rope Triceps Pushdown","Triceps","Lateral and medial heads","Long head","Cable, rope","Isolation",3,"10–15","60s","2-1-1",
       ["Stand close to the high pulley, slight forward lean.","Pin your elbows at your sides.","Push down and spread the rope apart at the bottom.","Return until your forearms are just above parallel."],
       [V(None,"cable-tricep-rope-grip-pushdown","pushdown","Cable Machine/Tricep/Cable Tricep Rope Grip Pushdown.mp4")]),
    ex("reverse-grip-pushdown","Reverse-Grip Cable Pushdown","Triceps","Medial head emphasis","Lateral head","Cable, straight bar","Isolation",2,"12–15","60s","2-1-2",
       ["Hold the bar underhand (palms up), hands shoulder-width.","Elbows stay pinned at your sides.","Push down to full extension.","Return slowly; use a lighter weight than the rope pushdown."],
       [V(None,None,"pushdown")],
       "Video not available: your pack only has the overhand pushdown. The drawing shows the elbow movement."),
   ]),
  ]),
 dict(day="Thursday", abbr="THU", focus="Back + Biceps", duration="70–85",
  tip="Vertical pull first for width, rows for thickness, then upper back and lower back. Keep back extensions moderate (2–3 reps in reserve) after Tuesday's squats and RDLs. Biceps go last.",
  muscles=[
   dict(name="Back", cls="m1", ex=[
    ex("pullup-pulldown","Pull-Up or Lat Pulldown","Back","Lats (width), teres major","Biceps, rear delts, lower traps","Pull-up bar or pulldown cable","Compound",3,"8–12","120s","3-1-1",
       ["Grip just outside shoulder-width.","Start from a full hang (or full stretch on the pulldown).","Pull your elbows down to your sides until your chin clears the bar or the bar reaches your upper chest.","Lower all the way under control."],
       [V("Pull-up","regular-pull-up","pullup","Bodyweight/Back/Regular Pull Up.mp4"), V("Lat pulldown","cable-pulldown","lat_pulldown","Cable Machine/Back/Cable Pulldown.mp4")]),
    ex("chest-supported-row","Chest-Supported Row (Seal Row)","Back","Mid back: rhomboids, middle traps","Lats, rear delts, biceps","Barbell, raised flat bench","Compound",3,"8–12","120s","2-1-1",
       ["Lie face down on a raised bench with the bar underneath you.","Grip slightly wider than shoulders.","Row the bar to the underside of the bench, squeezing your shoulder blades together.","Lower to a full stretch. Your chest stays on the bench."],
       [V(None,"barbell-seal-row",None,"Barbell/Back/Barbell Seal Row.mp4")]),
    ex("one-arm-cable-row","One-Arm Cable Row","Back","Lats and mid back","Rhomboids, biceps","Cable, single handle","Compound",2,"10–12","90s","2-1-2",
       ["Half-kneel facing a mid-height pulley.","Reach forward and let your shoulder stretch.","Row the handle to your hip, elbow close to your side.","Return slowly. Do all reps, then switch arms."],
       [V(None,"cable-half-kneeling-single-arm-row",None,"Cable Machine/Back/Cable Half Kneeling Single Arm Row.mp4")]),
    ex("face-pull","Cable Face Pull","Back","Upper back and rear delts","Middle/lower traps, rotator cuff","Cable, rope","Isolation",2,"12–15","60s","2-1-2",
       ["Set the rope at upper-chest to face height.","Pull the rope toward your face, splitting it apart.","Finish with your hands beside your ears and elbows high.","Return slowly."],
       [V(None,"cable-standing-face-pull","face_pull","Cable Machine/Shoulders/Cable Standing Face Pull.mp4")]),
    ex("back-extension","Back Extension","Back","Lower back (spinal erectors)","Glutes, hamstrings","Back extension machine (or 45° bench)","Isolation",2,"12–15","75s","2-1-2",
       ["Sit with the pad across your upper back and feet secured.","Brace your core.","Extend back until your body is straight; don't hyperextend.","Return slowly. Keep 2–3 reps in reserve."],
       [V(None,"lever-back-extension",None,"Gym Machine/Back/Lever Back Extension.mp4")]),
   ]),
   dict(name="Biceps", cls="m2", ex=[
    ex("incline-db-curl","Incline Dumbbell Curl","Biceps","Long head (arm behind the body)","Short head, brachialis","Dumbbells, incline bench","Isolation",3,"10–12","75s","3-1-1",
       ["Set the bench to about 45° and let your arms hang straight down.","Keep your shoulders back and upper arms still.","Curl the dumbbells up, turning your palms up.","Lower slowly to a full stretch."],
       [V(None,"incline-bicep-curl","incline_curl","Dumbbell/Bicep/Incline Bicep Curl.mp4")]),
    ex("preacher-curl","Preacher Curl","Biceps","Short head emphasis","Brachialis","EZ bar or barbell, preacher bench","Isolation",2,"10–12","75s","2-1-2",
       ["Rest the backs of your upper arms flat on the pad.","Start with your arms almost straight.","Curl up until your forearms are vertical.","Lower slowly; don't bounce out of the bottom."],
       [V(None,"barbell-seated-preacher-curl","preacher_curl","Barbell/Arm/Barbell Seated Preacher Curl.mp4")]),
    ex("hammer-curl","Seated Hammer Curl","Biceps","Brachialis and brachioradialis","Biceps","Dumbbells, bench","Isolation",2,"10–12","60s","2-1-2",
       ["Sit upright with the dumbbells at your sides, palms facing each other.","Keep your elbows still.","Curl up without turning your wrists.","Lower slowly."],
       [V(None,"seated-hammer-curl","hammer_curl","Dumbbell/Bicep/Seated Hammer Curl.mp4")],
       "Stands in for the rope hammer curl: same neutral grip, and your pack has no rope version."),
   ]),
  ]),
 dict(day="Friday", abbr="FRI", focus="Core + Obliques", duration="45–60",
  tip="Weighted flexion first, then lower-ab and hanging work, then rotation and stability. Upper and lower abs are regions of one muscle, so the variety is about angles, not separate muscles. Breathe out on the hard part of every rep.",
  muscles=[
   dict(name="Abs", cls="mc", ex=[
    ex("kneeling-cable-crunch","Kneeling Cable Crunch","Abs","Rectus abdominis, upper-region emphasis","Obliques","Cable, rope","Isolation",3,"12–15","60s","2-1-2",
       ["Kneel facing a high pulley with the rope beside your head.","Keep your hips still.","Crunch your ribs toward your hips, rounding your spine.","Squeeze, then return slowly."],
       [V(None,"kneeling-cable-crunch","cable_crunch","Cable Machine/ABS/Kneeling Cable Crunch.mp4")]),
    ex("reverse-crunch","Reverse Crunch","Abs","Rectus abdominis, lower-region emphasis","Hip flexors","Floor or bench","Isolation",3,"12–15","60s","2-1-2",
       ["Lie on your back with your knees bent at 90°.","Press your lower back into the floor.","Curl your hips up off the floor, knees toward your chest.","Lower slowly without swinging."],
       [V(None,"reverse-crunch",None,"Bodyweight/ABS/Reverse Crunch.mp4")]),
    ex("hanging-knee-raise","Hanging Knee Raise","Abs","Lower abs and hip flexors","Grip, obliques","Pull-up bar","Isolation",3,"10–15","75s","2-1-2",
       ["Hang from a bar with a shoulder-width grip.","Stop any swing before each rep.","Raise your knees toward your chest, tilting your pelvis up.","Lower slowly."],
       [V(None,None,"hanging_raise")],
       "Video not available: your pack has no hanging leg raise. The drawing shows the movement."),
   ]),
   dict(name="Obliques + Stability", cls="mc", ex=[
    ex("woodchopper","Cable Woodchopper","Obliques","External and internal obliques (rotation)","Transverse abdominis","Cable, single handle","Isolation",2,"12 per side","60s","2-1-2",
       ["Set a pulley high and stand side-on with feet wide.","Hold the handle with both hands, arms long.","Rotate through your torso and chop down across your body.","Return slowly. Do all reps, then switch sides."],
       [V(None,None,"woodchop")],
       "Video not available: your pack has no woodchopper. The drawing shows the movement."),
    ex("side-plank","Side Plank","Obliques","Lateral core (obliques, quadratus lumborum)","Glute medius","Floor (video shows the TRX version)","Stability",2,"30–45s per side","45s","hold",
       ["Lie on your side with your elbow under your shoulder.","Stack your feet and lift your hips.","Keep a straight line from head to heels.","Hold, breathing steadily, then switch sides."],
       [V(None,"trx-side-bridge","side_plank","TRX Suspension/ABS/TRX Side Bridge.mp4")],
       "The video shows a TRX side bridge, a harder version with the feet in straps. Do it with your feet on the floor unless you want the extra challenge."),
    ex("pallof-press","Pallof Press","Core","Anti-rotation, deep core (transverse abdominis)","Obliques","Cable (or band)","Stability",3,"12 per side","60s","2-2-2",
       ["Stand side-on to a chest-height pulley, handle at your chest.","Brace as if about to be pushed.","Press your hands straight out without letting your torso turn.","Hold for two seconds, bring back. Switch sides."],
       [V(None,None,"pallof")],
       "Video not available: your pack has no Pallof press. The drawing shows the movement."),
    ex("ab-wheel","Ab Wheel Rollout","Core","Anti-extension (whole rectus abdominis)","Lats, shoulders","Ab wheel (or TRX)","Stability",2,"8–12","75s","3-1-2",
       ["Kneel holding the wheel under your shoulders.","Brace and tuck your pelvis slightly.","Roll forward as far as you can without your lower back sagging.","Pull back with your abs, not your arms."],
       [V("Ab wheel",None,"ab_wheel"), V("TRX rollout","trx-ab-rollout","ab_wheel","TRX Suspension/ABS/TRX AB Rollout.mp4")],
       "Your pack has the TRX rollout but no ab wheel clip; both train the same anti-extension pattern."),
   ]),
  ]),
]

# old exercise names -> new exercise ids, so logged weights follow the exercise
LEGACY_MAP = {
 "Incline Barbell / Dumbbell Press":"incline-db-press","Overhead EZ Bar / Rope Extension":"overhead-cable-ext",
 "Rope Push Down / V-Bar Push Down":"rope-pushdown","Cable Crunch (Kneeling)":"kneeling-cable-crunch",
 "Wide Grip Pull-Up / Lat Pull Down":"pullup-pulldown","Incline Dumbbell Curl":"incline-db-curl",
 "Preacher Curl / Spider Curl":"preacher-curl","Hammer Curl / Cross Body Curl":"hammer-curl",
 "Hanging Knee / Leg Raises":"hanging-knee-raise","Ab Wheel Rollout":"ab-wheel",
 "Seated DB / Barbell Overhead Press":"seated-db-press","Dumbbell / Cable Lateral Raise":"cable-lateral-raise",
 "Rear Delt Fly / Reverse Pec Deck":"seated-db-reverse-fly","DB Front Raise / Cable Front Raise":"db-front-raise",
 "Incline DB Shrug":"db-shrug","Face Pull (Cable Rope)":"face-pull","Cable Face Pull":"face-pull",
 "Cable Woodchop (High to Low)":"woodchopper","Pallof Press (Cable)":"pallof-press",
 "Barbell Back Squat":"back-squat","Romanian Deadlift (RDL)":"rdl","Leg Extension":"leg-extension",
 "Nordic Curl / Lying Leg Curl":"lying-leg-curl","Standing + Seated Calf Raises":"standing-calf-raise",
 "Barbell / Cable Wrist Curl":"seated-wrist-curl","Reverse Barbell / EZ Bar Curl":"reverse-curl",
}

if __name__ == "__main__":
    ids = [e["id"] for d in PLAN for m in d["muscles"] for e in m["ex"]]
    assert len(ids) == len(set(ids)), "duplicate ids"
    assert all(v in ids for v in LEGACY_MAP.values())
    for d in PLAN:
        for m in d["muscles"]:
            for e in m["ex"]:
                for v in e["variants"]:
                    assert v["video"] or v["anim"], e["id"]
    open("plan.js", "w").write("const days = " + json.dumps(PLAN, ensure_ascii=False, separators=(",", ":")) + ";\n")
    print(len(ids), "exercises")

# ---------------------------------------------------------------------------
# Equipment settings. Each profile picks one; every slot uses its version for that setting when one
# exists, otherwise the slot's default (which works for everyone and is shown as a fallback).
MODES = {"free": "Dumbbells & barbells", "machines": "Machines & cables", "home": "Bodyweight & bands"}

CAT = {  # category of each default exercise; "any" = fits every setting
 "seated-db-press":"free","cable-lateral-raise":"machines","seated-db-reverse-fly":"free","db-front-raise":"free",
 "db-shrug":"free","seated-wrist-curl":"free","reverse-wrist-curl":"free","reverse-curl":"machines",
 "back-squat":"free","leg-extension":"machines","rdl":"free","hip-thrust":"free","lying-leg-curl":"machines",
 "cable-hip-abduction":"machines","hip-adduction":"machines","standing-calf-raise":"machines","seated-calf-raise":"machines","tibialis-raise":"any",
 "incline-db-press":"free","flat-bb-bench":"free","decline-machine-press":"machines","cable-fly-high-low":"machines",
 "overhead-cable-ext":"machines","rope-pushdown":"machines","reverse-grip-pushdown":"machines",
 "pullup-pulldown":"any","chest-supported-row":"free","one-arm-cable-row":"machines","face-pull":"machines","back-extension":"machines",
 "incline-db-curl":"free","preacher-curl":"free","hammer-curl":"free",
 "kneeling-cable-crunch":"machines","reverse-crunch":"home","hanging-knee-raise":"home","woodchopper":"machines",
 "side-plank":"home","pallof-press":"machines","ab-wheel":"any",
}

def A(id, name, cat, equipment, variants, steps, notes=""):
    return dict(id=id, name=name, cat=cat, equipment=equipment, variants=variants, steps=steps, alts=notes)

BAND_HAMMER = A("band-hammer-curl","Band Hammer Curl","home","Resistance band",[V(None,"band-hammer-curl","hammer_curl","Resistance Band/Bicep/Band Hammer Curl.mp4")],
  ["Stand on the band, ends in each hand, palms facing each other.","Pin your elbows to your sides.","Curl up without rotating your wrists.","Lower slowly against the band."])

ALTS = {
 # Monday
 "seated-db-press": {
  "machines": A("cable-shoulder-press","Seated Cable Shoulder Press","machines","Cable, two low pulleys, bench",[V(None,"cable-seated-shoulders-press","ohp_front","Cable Machine/Shoulders/Cable Seated Shoulders Press.mp4")],
    ["Sit upright between two low pulleys, handles at shoulder height.","Brace your core and keep your back tall.","Press up and slightly in until your arms are nearly straight.","Lower slowly back to shoulder height."]),
  "home": A("band-shoulder-press","Band Shoulder Press","home","Resistance band",[V(None,"band-shoulders-press","ohp_front","Resistance Band/Shoulders/Band Shoulders Press.mp4")],
    ["Stand on the band, handles or ends at shoulder height.","Brace your core and squeeze your glutes.","Press overhead until your arms are straight.","Lower slowly to shoulder height."])},
 "cable-lateral-raise": {
  "free": A("db-lateral-raise","Leaning Dumbbell Lateral Raise","free","Dumbbell, post to hold",[V(None,"dumbbell-leaning-lateral-raise","lateral_raise","Dumbbell/Shoulders/Dumbbell Leaning Lateral Raise.mp4")],
    ["Hold a post with one hand and lean slightly away.","Raise the dumbbell out to the side with a soft elbow.","Stop at shoulder height; lead with the elbow.","Lower slowly. Switch sides."]),
  "home": A("band-lateral-raise","Band Lateral Raise","home","Resistance band",[V(None,"band-one-arm-lateral-raise","lateral_raise","Resistance Band/Shoulders/Band One Arm Lateral Raise.mp4")],
    ["Stand on one end of the band and hold the other across your body.","Raise your arm out to the side to shoulder height.","Pause, then lower slowly.","Do all reps, then switch sides."])},
 "seated-db-reverse-fly": {
  "machines": A("cable-reverse-fly","Cable Reverse Fly","machines","Cable, single handle",[V(None,"cable-one-arm-reverse-fly","rear_fly_cable","Cable Machine/Shoulders/Cable One Arm Reverse Fly.mp4")],
    ["Stand side-on to a low pulley and hinge forward slightly.","Hold the handle with the far hand across your body.","Sweep the arm out and back to shoulder height.","Return slowly. Switch sides."]),
  "home": A("band-reverse-fly","Band Bent-Over Reverse Fly","home","Resistance band",[V(None,"band-bent-over-reverse-fly","rear_fly_top","Resistance Band/Shoulders/Band Bent Over Reverse Fly.mp4")],
    ["Stand on the band with the ends crossed, hinge forward.","Arms hang under your shoulders, elbows soft.","Open your arms out wide, squeezing the backs of your shoulders.","Return slowly."])},
 "db-front-raise": {
  "machines": A("cable-front-raise","Cable Front Raise","machines","Cable, low pulley",[V(None,"cable-shoulders-front-raise","front_raise","Cable Machine/Shoulders/Cable Shoulders Front Raise.mp4")],
    ["Face away from a low pulley, handle between your legs.","Raise your arm forward to shoulder height, elbow soft.","Don't lean back.","Lower slowly."]),
  "home": A("band-front-raise","Band Front Raise","home","Resistance band",[V(None,"band-front-raise","front_raise","Resistance Band/Shoulders/Band Front Raise.mp4")],
    ["Stand on the band, ends in front of your thighs.","Raise forward to shoulder height.","Pause briefly.","Lower slowly."])},
 "db-shrug": {
  "machines": A("smith-shrug","Smith Machine Shrug","machines","Smith machine",[V(None,"smith-shrug","shrug","Smith Machine/Back/Smith Shrug.mp4")],
    ["Stand tall holding the bar at arm's length.","Lift your shoulders straight up toward your ears.","Hold the top for a second.","Lower all the way down."]),
  "home": A("band-shrug","Band Shrug","home","Resistance band",[V(None,"band-shrug","shrug_db","Resistance Band/Back/Band Shrug.mp4")],
    ["Stand on the band with the ends in your hands.","Lift your shoulders straight up.","Hold the top for two seconds.","Lower slowly."])},
 "reverse-curl": {
  "free": A("reverse-ez-curl","Reverse EZ-Bar Curl","free","EZ bar or barbell",[V(None,None,"reverse_curl")],
    ["Hold the bar overhand, hands shoulder-width.","Keep your elbows pinned at your sides.","Curl up until your forearms are vertical, wrists straight.","Lower slowly."],
    "Video not available for the barbell version. The drawing shows the movement; the cable video under Machines shows the same grip."),
  "home": BAND_HAMMER},
 # Tuesday
 "back-squat": {
  "machines": A("hack-squat","Hack Squat","machines","Hack squat machine",[V(None,"sled-full-hack-squat",None,"Gym Machine/Legs/Sled Full Hack Squat.mp4")],
    ["Shoulders under the pads, feet shoulder-width in the middle of the platform.","Release the safeties and brace.","Lower until your thighs are at least parallel.","Drive up through your whole foot."]),
  "home": A("band-squat","Band Squat","home","Resistance band",[V(None,"band-squat","squat","Resistance Band/Legs/Band Squat.mp4")],
    ["Stand on the band with it looped over your shoulders.","Feet shoulder-width, chest up.","Squat down until your thighs are parallel.","Drive up against the band."])},
 "leg-extension": {
  "free": A("db-split-squat","Dumbbell Split Squat","free","Dumbbells",[V(None,"dumbbell-split-squat","bulgarian","Dumbbell/Legs/Dumbbell Split Squat.mp4")],
    ["Hold dumbbells at your sides in a long split stance.","Keep your torso upright.","Lower your back knee toward the floor.","Push through your front foot. Do all reps, then switch legs."],
    "There's no dumbbell leg extension, so this quad-focused split squat takes its place."),
  "home": A("split-squat","Split Squat","home","Bodyweight",[V(None,"split-squat","bulgarian","Bodyweight/Legs/Split Squat.mp4")],
    ["Stand in a long split stance.","Keep your torso upright.","Lower your back knee toward the floor.","Push through your front foot. Switch legs."])},
 "rdl": {
  "machines": A("cable-rdl","Cable Romanian Deadlift","machines","Cable, low pulley",[V(None,"cable-romanian-deadlift","rdl","Cable Machine/Legs/Cable Romanian Deadlift.mp4")],
    ["Face a low pulley holding the handle or bar.","Soft knees, push your hips back.","Lower until your hamstrings are stretched, back flat.","Drive your hips forward to stand."]),
  "home": A("band-rdl","Band Romanian Deadlift","home","Resistance band",[V(None,"band-romanian-deadlift","rdl","Resistance Band/Legs/Band Romanian Deadlift.mp4")],
    ["Stand on the band, ends in your hands.","Soft knees, push your hips back.","Lower until your hamstrings are stretched.","Drive your hips forward against the band."])},
 "hip-thrust": {
  "machines": A("machine-hip-thrust","Machine Hip Thrust","machines","Hip thrust machine",[V(None,"lever-hip-thrust",None,"Gym Machine/Legs/Lever Hip Thrust.mp4")],
    ["Set the pad across your hips, upper back on the backrest.","Feet flat, hip-width.","Drive your hips up until level with your shoulders.","Squeeze for two seconds, then lower."]),
  "home": A("band-glute-bridge","Band Glute Bridge","home","Resistance band (loop)",[V(None,"band-glute-bridge",None,"Resistance Band/Legs/Band Glute Bridge.mp4")],
    ["Lie on your back with a band just above your knees.","Feet flat, knees pushed out against the band.","Drive your hips up and squeeze your glutes.","Lower slowly."])},
 "lying-leg-curl": {
  "home": A("band-leg-curl","Band Lying Leg Curl","home","Resistance band",[V(None,"band-lying-leg-curl","lying_leg_curl","Resistance Band/Legs/Band Lying Leg Curl.mp4")],
    ["Lie face down with the band anchored low and looped around your ankles.","Keep your hips on the floor.","Curl your heels toward your glutes.","Lower slowly."])},
 "standing-calf-raise": {
  "home": A("bw-calf-raise","Standing Calf Raise (bodyweight)","home","Bodyweight, step",[V(None,"calf-raise","calf_raise","Bodyweight/Legs/Calf Raise.mp4")],
    ["Stand on the edge of a step, holding something for balance.","Rise as high as you can.","Pause at the top.","Lower your heels below the step. Do single legs to make it harder."])},
 "seated-calf-raise": {
  "free": A("db-seated-calf-raise","Dumbbell Seated Calf Raise","free","Dumbbells, bench, step",[V(None,"dumbbell-seated-calf-raise",None,"Dumbbell/Legs/Dumbbell Seated Calf Raise.mp4")],
    ["Sit with the balls of your feet on a step, dumbbells on your knees.","Let your heels drop.","Push up onto your toes and hold.","Lower slowly."]),
  "home": None},  # filled below with the dumbbell version
 # Wednesday
 "incline-db-press": {
  "machines": A("machine-incline-press","Incline Machine Chest Press","machines","Incline press machine",[V(None,"lever-incline-chest-press","incline_press","Gym Machine/Chest/Lever Incline Chest Press.mp4")],
    ["Set the seat so the handles line up with your upper chest.","Back on the pad, shoulder blades pinched.","Press up and forward until your arms are nearly straight.","Return slowly to a stretch."]),
  "home": A("decline-push-up","Decline Push-Up (feet raised)","home","Bodyweight, bench",[V(None,"decline-push-up",None,"Bodyweight/Chest/Decline Push Up.mp4")],
    ["Feet on a bench, hands on the floor slightly wider than shoulders.","Body in a straight line.","Lower your chest toward the floor.","Push back up. Raising your feet shifts work to the upper chest."])},
 "flat-bb-bench": {
  "machines": A("machine-chest-press","Machine Chest Press","machines","Chest press machine",[V(None,"lever-chest-press","flat_bb_press","Gym Machine/Chest/Lever Chest Press.mp4")],
    ["Set the seat so the handles are at mid-chest.","Back on the pad, shoulder blades pinched.","Press forward until your arms are nearly straight.","Return slowly."]),
  "home": A("push-up","Push-Up","home","Bodyweight",[V(None,"regular-push-up",None,"Bodyweight/Chest/Regular Push Up.mp4")],
    ["Hands slightly wider than your shoulders, body in a straight line.","Lower your chest to just above the floor.","Elbows about 45° from your body.","Push back up. Add a band across your back to make it harder."])},
 "decline-machine-press": {
  "free": A("db-decline-press","Decline Dumbbell Press","free","Dumbbells, decline bench",[V(None,"dumbbell-decline-bench-press","decline_press","Dumbbell/Chest/Dumbbell Decline Bench Press.mp4")],
    ["Secure your feet on a decline bench.","Start with the dumbbells over your lower chest.","Lower to the sides of your lower chest.","Press up and slightly in."]),
  "home": A("chest-dip","Chest Dip","home","Parallel bars",[V(None,"chest-dip","dips","Bodyweight/Chest/Chest Dip.mp4")],
    ["Support yourself on parallel bars.","Lean your torso forward slightly.","Lower until your shoulders are just below your elbows.","Press back up."])},
 "cable-fly-high-low": {
  "free": A("db-fly","Dumbbell Fly","free","Dumbbells, flat or decline bench",[V(None,"dumbbell-bench-fly","fly_top","Dumbbell/Chest/Dumbbell Bench Fly.mp4")],
    ["Lie on the bench with the dumbbells above your chest, elbows soft.","Open your arms wide in an arc.","Stop at a deep stretch, level with your chest.","Squeeze back up. Use a slight decline for more lower chest."]),
  "home": A("trx-chest-fly","TRX Chest Fly","home","Suspension trainer",[V(None,"trx-chest-fly","fly_top","TRX Suspension/Chest/TRX Chest Fly.mp4")],
    ["Face away from the anchor, arms out in front holding the handles.","Lean forward into the straps, body straight.","Open your arms wide, lowering your chest.","Squeeze your arms back together."])},
 "overhead-cable-ext": {
  "free": A("db-overhead-ext","Seated Dumbbell Overhead Extension","free","Dumbbell, bench",[V(None,"dumbbell-seated-tricep-extension","overhead_ext_db","Dumbbell/Tricep/Dumbbell Seated Tricep Extension.mp4")],
    ["Sit upright holding one dumbbell overhead with both hands.","Elbows point forward, close to your head.","Lower behind your head to a deep stretch.","Extend back up."]),
  "home": A("band-overhead-ext","Band Overhead Extension","home","Resistance band",[V(None,"band-overhead-tricep-extension","overhead_ext","Resistance Band/Tricep/Band Overhead Tricep Extension.mp4")],
    ["Stand on the band, ends behind your head.","Elbows point up, close to your head.","Extend your arms overhead.","Lower slowly behind your head."])},
 "rope-pushdown": {
  "free": A("db-skull-crusher","Dumbbell Skull Crusher","free","Dumbbells, flat bench",[V(None,"dumbbell-bench-lying-tricep-extension",None,"Dumbbell/Tricep/Dumbbell Bench Lying Tricep Extension.mp4")],
    ["Lie on a bench with the dumbbells above your shoulders.","Keep your upper arms still.","Bend your elbows to lower the dumbbells beside your head.","Extend back up."]),
  "home": A("band-pushdown","Band Rope Pushdown","home","Resistance band, high anchor",[V(None,"band-rope-tricep-pushdown","pushdown","Resistance Band/Tricep/Band Rope Tricep Pushdown.mp4")],
    ["Anchor the band high and hold the ends.","Pin your elbows at your sides.","Push down to full extension.","Return slowly."])},
 "reverse-grip-pushdown": {
  "free": A("db-kickback","Dumbbell Triceps Kickback","free","Dumbbell, bench",[V(None,"dumbbell-tricep-kickback",None,"Dumbbell/Tricep/Dumbbell Tricep Kickback.mp4")],
    ["Hinge forward with your upper arm parallel to the floor.","Keep your upper arm still.","Extend your elbow until your arm is straight.","Squeeze, then lower slowly."]),
  "home": A("bench-dip","Bench Dip","home","Bench or chair",[V(None,"bench-dip",None,"Bodyweight/Arm and Shoulders/Bench Dip.mp4")],
    ["Hands on a bench behind you, legs out in front.","Lower until your elbows are at 90°.","Keep your back close to the bench.","Press back up."])},
 # Thursday
 "pullup-pulldown": {
  "machines": A("lat-pulldown","Lat Pulldown","machines","Pulldown cable or machine",[V("Cable pulldown","cable-pulldown","lat_pulldown","Cable Machine/Back/Cable Pulldown.mp4"),V("Machine pulldown","lever-pulldown","lat_pulldown","Gym Machine/Back/Lever Pulldown.mp4")],
    ["Grip just outside shoulder-width, thighs under the pad.","Start from a full stretch.","Pull your elbows down to your sides, bar to your upper chest.","Return slowly to a full stretch."]),
  "home": A("pull-up","Pull-Up","home","Pull-up bar (band for assistance)",[V("Pull-up","regular-pull-up","pullup","Bodyweight/Back/Regular Pull Up.mp4"),V("Band-assisted","band-assisted-pull-up","pullup","Resistance Band/Back/Band Assisted Pull Up.mp4")],
    ["Grip just outside shoulder-width.","Start from a full hang.","Pull until your chin clears the bar.","Lower all the way. Use a band under your feet or knees if you need help."])},
 "chest-supported-row": {
  "machines": A("machine-chest-row","Chest-Supported Machine Row","machines","Row machine with chest pad",[V(None,"lever-seated-grip-row",None,"Gym Machine/Back/Lever Seated Grip Row.mp4")],
    ["Chest against the pad, arms reaching forward.","Row the handles back, squeezing your shoulder blades.","Pause for a second.","Return to a full stretch."]),
  "home": A("inverted-row","Inverted Row","home","Bar or rings at hip height",[V(None,"inverted-row","seated_row","Bodyweight/Back/Inverted Row.mp4")],
    ["Hang under a bar with your body straight, heels on the floor.","Pull your chest to the bar.","Squeeze your shoulder blades together.","Lower slowly. Bend your knees to make it easier."])},
 "one-arm-cable-row": {
  "free": A("db-one-arm-row","One-Arm Dumbbell Row","free","Dumbbell, bench",[V(None,"dumbbell-bench-one-arm-row","db_row","Dumbbell/Back/Dumbbell Bench One Arm Row.mp4")],
    ["One knee and hand on the bench, back flat.","Let the dumbbell hang to a full stretch.","Row it to your hip, elbow close to your side.","Lower slowly. Switch sides."]),
  "home": A("band-kneeling-row","Half-Kneeling Band Row","home","Resistance band, anchor",[V(None,"band-half-kneeling-row","seated_row","Resistance Band/Back/Band Half Kneeling Row.mp4")],
    ["Half-kneel facing the anchor, band in one hand.","Reach forward to a stretch.","Row to your hip.","Return slowly. Switch sides."])},
 "face-pull": {
  "free": A("db-rear-delt-row","Seated Dumbbell Rear Delt Row","free","Dumbbells, bench",[V(None,"dumbbell-seated-rear-delt-row",None,"Dumbbell/Shoulders/Dumbbell Seated Rear Delt Row.mp4")],
    ["Sit and hinge forward, dumbbells hanging.","Row with your elbows flared wide.","Squeeze your upper back and rear delts.","Lower slowly."]),
  "home": A("band-face-pull","Band Face Pull","home","Resistance band, anchor",[V(None,"band-half-kneeling-face-pull","face_pull","Resistance Band/Shoulders/Band Half Kneeling Face Pull.mp4")],
    ["Anchor the band at head height.","Pull toward your face, hands splitting apart.","Finish with elbows high, hands by your ears.","Return slowly."])},
 "back-extension": {
  "free": A("db-good-morning","Dumbbell Good Morning","free","Dumbbell",[V(None,"dumbbell-good-morning","rdl","Dumbbell/Legs/Dumbbell Good Morning.mp4")],
    ["Hold a dumbbell against your chest.","Soft knees, push your hips back.","Hinge until your torso is nearly parallel, back flat.","Stand up by driving your hips forward. Go light after Tuesday's legs."]),
  "home": A("lying-back-extension","Lying Back Extension","home","Floor",[V(None,"lying-back-extension",None,"Bodyweight/Back/Lying Back Extension.mp4")],
    ["Lie face down, hands by your head.","Lift your chest off the floor using your lower back.","Pause for a second.","Lower slowly."])},
 "incline-db-curl": {
  "machines": A("cable-bayesian-curl","Bayesian Cable Curl","machines","Cable, low pulley",[V(None,"cable-bayesian-bicep-curl","incline_curl","Cable Machine/Bicep/Cable Bayesian Bicep Curl.mp4")],
    ["Face away from a low pulley, arm reaching back behind you.","Keep your upper arm behind your body.","Curl up, palm facing up.","Lower slowly to a full stretch. Switch arms."],
    "Same long-head stretch as the incline curl."),
  "home": A("band-bayesian-curl","Bayesian Band Curl","home","Resistance band, anchor",[V(None,"band-bayesian-bicep-curl","incline_curl","Resistance Band/Bicep/Band Bayesian Bicep Curl.mp4")],
    ["Face away from a low anchor, arm reaching back.","Keep your upper arm behind your body.","Curl up.","Lower slowly. Switch arms."])},
 "preacher-curl": {
  "machines": A("cable-spider-curl","Cable Spider Curl","machines","Cable, incline bench",[V(None,"cable-spider-bicep-curl",None,"Cable Machine/Bicep/Cable Spider Bicep Curl.mp4")],
    ["Lie chest-down on an incline bench facing a low pulley.","Let your arms hang straight down.","Curl up without moving your upper arms.","Lower slowly."],
    "Arms in front of the body, like the preacher curl, for short-head emphasis."),
  "home": A("band-curl","Band Biceps Curl","home","Resistance band",[V(None,"band-bicep-curl","hammer_curl","Resistance Band/Bicep/Band Bicep Curl.mp4")],
    ["Stand on the band, palms facing forward.","Pin your elbows to your sides.","Curl up and squeeze.","Lower slowly."])},
 "hammer-curl": {
  "machines": A("cable-preacher-hammer","Cable Preacher Hammer Curl","machines","Cable, rope, preacher bench",[V(None,"cable-preacher-hammer-curl","preacher_curl","Cable Machine/Bicep/Cable Preacher Hammer Curl.mp4")],
    ["Upper arms on the preacher pad, rope from a low pulley.","Neutral grip, palms facing each other.","Curl up without turning your wrists.","Lower slowly."]),
  "home": BAND_HAMMER},
 # Friday
 "kneeling-cable-crunch": {
  "free": A("db-weighted-crunch","Weighted Crunch","free","Dumbbell or plate",[V(None,"dumbbell-weighted-crunch",None,"Dumbbell/ABS/Dumbbell Weighted Crunch.mp4")],
    ["Lie on your back, knees bent, weight held above your chest.","Curl your ribs toward your hips.","Squeeze for a second.","Lower slowly."]),
  "home": A("band-kneeling-crunch","Band Kneeling Crunch","home","Resistance band, high anchor",[V(None,"band-kneeling-crunch","cable_crunch","Resistance Band/ABS/Band Kneeling Crunch.mp4")],
    ["Kneel facing a high anchor, band ends by your head.","Keep your hips still.","Crunch your ribs toward your hips.","Return slowly."])},
 "reverse-crunch": {
  "machines": A("cable-reverse-crunch","Cable Reverse Crunch","machines","Cable, ankle strap",[V(None,"cable-reverse-crunch",None,"Cable Machine/ABS/Cable Reverse Crunch.mp4")],
    ["Lie on your back with the cable strapped to your feet.","Knees bent at 90°.","Curl your hips up toward your chest.","Lower slowly against the cable."])},
 "hanging-knee-raise": {
  "machines": A("cable-lying-leg-raise","Cable Lying Leg Raise","machines","Cable, ankle strap",[V(None,"cable-lying-leg-raise",None,"Cable Machine/ABS/Cable Lying Leg Raise.mp4")],
    ["Lie on your back with the cable strapped to your ankles.","Press your lower back into the floor.","Raise your legs to vertical.","Lower slowly without arching."])},
}
ALTS["seated-calf-raise"]["home"] = ALTS["seated-calf-raise"]["free"]

SHARED = ("primary","tgt","secondary","kind","sets","reps","rest","tempo")

def build():
    out = json.loads(json.dumps(PLAN))
    for d in out:
        for m in d["muscles"]:
            for e in m["ex"]:
                e["cat"] = CAT[e["id"]]
                opts = {}
                for mode, alt in ALTS.get(e["id"], {}).items():
                    if alt is None: continue
                    a = dict(alt); [a.setdefault(k, e[k]) for k in SHARED]
                    if a["cat"] == "home" and a["kind"] == "Compound":
                        # bands and bodyweight are lighter than barbells: more reps, shorter rest
                        a["reps"], a["rest"] = "12–20", "90s"
                        a["alts"] = (a.get("alts") + " " if a.get("alts") else "") + "Reps are higher than the weighted version because bands and bodyweight are lighter. Make it harder (thicker band, slower tempo, pause at the bottom) once 20 reps feel easy."
                    opts[mode] = a
                e["opts"] = opts
    return out

def resolve(e, mode):
    return e["opts"].get(mode) or e

if __name__ == "__main__":
    P = build()
    for mode, label in MODES.items():
        tot = fit = 0
        for d in P:
            row = [resolve(e, mode) for m in d["muscles"] for e in m["ex"]]
            tot += len(row); fit += sum(1 for x in row if x["cat"] in (mode, "any"))
        print(f"{label}: {fit}/{tot} exercises in the chosen category")
    vids = sorted({v["video"] for d in P for m in d["muscles"] for e in m["ex"] for x in [e]+list(e["opts"].values()) for v in x["variants"] if v["video"]})
    srcs = {v["video"]: v["src"] for d in P for m in d["muscles"] for e in m["ex"] for x in [e]+list(e["opts"].values()) for v in x["variants"] if v["video"]}
    json.dump(srcs, open("all_srcs.json", "w"), indent=0)
    open("plan.js", "w").write("const days = " + json.dumps(P, ensure_ascii=False, separators=(",", ":")) + ";\nconst MODES = " + json.dumps(MODES) + ";\n")
    print(len(vids), "distinct clips referenced")
