import React, { useEffect } from "react";
import { Helmet } from "react-helmet";

/*
 * The workout tracker is a self-contained app in public/5-Day-Split-App.html
 * (it can also be added to a phone's home screen on its own).
 * This page shows it full-screen inside the site.
 */
const Workouts = () => {
	useEffect(() => {
		window.scrollTo(0, 0);
	}, []);

	return (
		<React.Fragment>
			<Helmet>
				<title>Workouts | Sandeep Varma</title>
			</Helmet>
			<iframe
				src="/5-Day-Split-App.html"
				title="5-Day Split workout tracker"
				style={{
					display: "block",
					border: "none",
					width: "100%",
					height: "100vh",
					minHeight: "100dvh",
				}}
			/>
		</React.Fragment>
	);
};

export default Workouts;
