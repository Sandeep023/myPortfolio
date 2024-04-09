import { useEffect } from "react";
import { Routes, Route } from "react-router-dom";
import ReactGA from "react-ga4";

import Homepage from "./pages/homepage";
import About from "./pages/about";
import Projects from "./pages/projects";
import Articles from "./pages/articles";
import ReadArticle from "./pages/readArticle";
import Contact from "./pages/contact";
import Notfound from "./pages/404";
import Expierience from "./pages/expierience";

import { TRACKING_ID } from "./data/tracking";
import "./app.css";

function App() {
	useEffect(() => {
		if (TRACKING_ID !== "") {
			ReactGA.initialize(TRACKING_ID);
		}
	}, []);

	return (
		<div className="App">
			<Routes>
				<Route path="/" element={<Homepage />} />
				<Route path="/myPortfolio" element={<Homepage />} />
				<Route path="/about" element={<About />} />
				<Route path="/myPortfolio/about" element={<About />} />
				<Route path="/projects" element={<Projects />} />
				<Route path="/myPortfolio/projects" element={<Projects />} />
				{/* <Route path="/articles" element={<Articles />} /> */}
				<Route path="/expierience" element={<Expierience />} />
				<Route path="/myPortfolio/expierience" element={<Expierience />} />
				<Route path="/article/:slug" element={<ReadArticle />} />
				<Route path="/contact" element={<Contact />} />
				<Route path="/myPortfolio/contact" element={<Contact />} />
				<Route path="*" element={<Notfound />} />
			</Routes>
		</div>
	);
}

export default App;

//https://github.com/truethari/reactfolio?tab=readme-ov-file
//https://github.com/topics/react-portfolio-template