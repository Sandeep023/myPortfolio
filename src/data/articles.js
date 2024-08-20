import React from "react";

function article_1() {
	return {
		date: "10 August 2024",
		title: "Creating your own Portfolio, AWS, React",
		description:
			"This article will give you a basic idea on how to deploy your ReactJS app in AWS EC2, with your own domain name.",
		keywords: [
			"ReactJS", "React", "AWS", "AWS EC2", "AWS Route 53"
		],
		link: `https://medium.com/@sandeepvarma531/host-your-profile-in-the-aws-ec2-instance-and-link-it-to-your-domain-url-c7e7bc91a70f`,
		style: `
				.article-content {
					display: flex;
					flex-direction: column;
					align-items: center;
				}

				.randImage {
					align-self: center;
					outline: 2px solid red;
				}
				`,
		body: (
			<React.Fragment>
				<div className="article-content">
					<div className="paragraph">Content of article 1</div>
					<img
						src="https://picsum.photos/200/300"
						alt="random"
						className="randImage"
					/>
				</div>
			</React.Fragment>
		),
	};
}

function article_2() {
	return {
		date: "7 May 2023",
		title: "Artificial Intelligence in Healthcare",
		description:
			"AI is transforming the healthcare industry, from improving patient outcomes to streamlining operations. Discover the latest applications of this game-changing technology.",
		style: ``,
		keywords: [
			"Artificial Intelligence in Healthcare",
			"Tharindu",
			"Tharindu N",
			"Tharindu Nayanajith",
		],
		body: (
			<React.Fragment>
				<h1>Content of article 2</h1>
			</React.Fragment>
		),
	};
}

const myArticles = [article_1];

export default myArticles;
