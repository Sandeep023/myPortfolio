import React from "react";
import { faBriefcase } from "@fortawesome/free-solid-svg-icons";

import Card from "../common/card";

import "./styles/works.css";

const Works = () => {
	return (
		<div className="works">
			<Card
				icon={faBriefcase}
				title="Expierience"
				body={
					<div className="works-body">
						<div className="work">
							{/* <img
								src="./facebook.png"
								alt="facebook"
								className="work-image"
							/> */}
							<div className="work-title">Adept Consulting</div>
							<div className="work-subtitle">
								Full-Stack Developer
							</div>
							<div className="work-duration">2023 APR - Present</div>
						</div>

						<div className="work">
							{/* <img
								src="./twitter.png"
								alt="twitter"
								className="work-image"
							/> */}
							<div className="work-title">Covit INC</div>
							<div className="work-subtitle">
								Full-Stack Developer - Intern
							</div>
							<div className="work-duration">2022 JUN - 2022 AUG</div>
						</div>

						<div className="work">
							{/* <img
								src="./twitter.png"
								alt="twitter"
								className="work-image"
							/> */}
							<div className="work-title">Thingks Infomatics</div>
							<div className="work-subtitle">
								Full-Stack Developer | Data Engineer
							</div>
							<div className="work-duration">2018 JUN - 2020 DEC</div>
						</div>
					</div>
				}
			/>
		</div>
	);
};

export default Works;
