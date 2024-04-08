import React from "react";
import { faBriefcase, faCertificate } from "@fortawesome/free-solid-svg-icons";

import Card from "../common/card";

import "./styles/works.css";

const Educations = () => {
	return (
		<div className="works">
			<Card
				icon={faCertificate}
				title="Education"
				body={
					<div className="works-body">
						<div className="work">
							{/* <img
								src="./facebook.png"
								alt="facebook"
								className="work-image"
							/> */}
							<div className="work-title">Texas A&M Unversity-Corpus Christi</div>
							<div className="work-subtitle">
								Master's in Computer Science
							</div>
							<div className="work-duration">2021 JAN - 2022 DEC</div>
						</div>

						<div className="work">
							{/* <img
								src="./twitter.png"
								alt="twitter"
								className="work-image"
							/> */}
							<div className="work-title">Indian Institute of Information Technology-Sricity</div>
							<div className="work-subtitle">
								B.Tech in Computer Science
							</div>
							<div className="work-duration">2014 AUG - 2018 MAY</div>
						</div>
					</div>
				}
			/>
		</div>
	);
};

export default Educations;
