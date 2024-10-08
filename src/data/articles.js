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
		date: "05 Oct 2024",
		title: "Navigating AWS: Key Insights from My Udemy Course Experience",
		description:
			"As I delve deeper into the world of Amazon Web Services (AWS), I’ve taken on the challenge of summarizing my learnings from the “AWS Certified Developer — Associate” course on Udemy. My goal is to distill key concepts and highlights into digestible notes that can serve as quick references for fellow developers.",
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
		link: `https://medium.com/@sandeepvarma531/navigating-aws-key-insights-from-my-udemy-course-experience-48cb49c4ae69`,
		keywords: [
		],
		body: (
			<React.Fragment>
				<h1>Content of article 2</h1>
			</React.Fragment>
		),
	};
}

function article_3() {
	return {
		date: "07 Oct 2024",
		title: "Mastering AWS IAM: Essential Guide for Developers",
		description:
			"Navigating the complexities of AWS Identity and Access Management (IAM) can seem daunting. Whether you’re new to AWS or looking to tighten your security practices, understanding IAM is crucial. This guide, based on expert insights, demystifies IAM, empowering developers with the knowledge to secure their AWS environments effectively.",
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
		link: `https://medium.com/@sandeepvarma531/mastering-aws-iam-essential-guide-for-developers-03e9264980ac`,
		keywords: [
		],
		body: (
			<React.Fragment>
				<h1>Content of article 2</h1>
			</React.Fragment>
		),
	};
}

const myArticles = [article_2, article_3, article_1];

export default myArticles;
