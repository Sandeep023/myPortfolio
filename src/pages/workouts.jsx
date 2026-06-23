import React, { useEffect } from "react";
import { Helmet } from "react-helmet";

import NavBar from "../components/common/navBar";
import Footer from "../components/common/footer";
import Logo from "../components/common/logo";
import Socials from "../components/about/socials";

import INFO from "../data/user";
import SEO from "../data/seo";

import "./styles/about.css";

const Workouts = () => {
	useEffect(() => {
		window.scrollTo(0, 0);
	}, []);

	return (
        <iframe
            src="./5-Day-Split-App.html"
            title="External HTML Document"
            width="100%" 
            height="100%"
            style={{ border: 'none', height: "1000px" }}
        />
	);
};

export default Workouts;
