import React from "react";
import { Link } from "react-router-dom";

import "./styles/navBar.css";

const NavBar = (props) => {
	const { active } = props;

	return (
		<React.Fragment>
			<div className="nav-container">
				<nav className="navbar">
					<div className="nav-background">
						<ul className="nav-list">
							<li
								className={
									active === "home"
										? "nav-item active"
										: "nav-item"
								}
							>
								<Link to="/myPortfolio/">Home</Link>
							</li>
							<li
								className={
									active === "about"
										? "nav-item active"
										: "nav-item"
								}
							>
								<Link to="/myPortfolio/about">About</Link>
							</li>
							<li
								className={
									active === "projects"
										? "nav-item active"
										: "nav-item"
								}
							>
								<Link to="/myPortfolio/projects">Projects</Link>
							</li>
							<li
								className={
									active === "expierience"
										? "nav-item active"
										: "nav-item"
								}
							>
								<Link to="/myPortfolio/expierience">Expierience</Link>
							</li>
							{/* <li
								className={
									active === "articles"
										? "nav-item active"
										: "nav-item"
								}
							>
								<Link to="/articles">Articles</Link>
							</li> */}
							<li
								className={
									active === "contact"
										? "nav-item active"
										: "nav-item"
								}
							>
								<Link to="/myPortfolio/contact">Contact</Link>
							</li>
							<li
								className={
									active === "resume"
										? "nav-item active"
										: "nav-item"
								}
							>
								<Link target="_blank" to="https://drive.google.com/file/d/16oSaJgE8x9SvWhpA0VTxDNr1N0AXHuDV/view?usp=share_link">
									Resume</Link>
							</li>
						</ul>
					</div>
				</nav>
			</div>
		</React.Fragment>
	);
};

export default NavBar;
