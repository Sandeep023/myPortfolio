import React from "react";

import Timeline from '@mui/lab/Timeline';
import TimelineItem from '@mui/lab/TimelineItem';
import TimelineSeparator from '@mui/lab/TimelineSeparator';
import TimelineConnector from '@mui/lab/TimelineConnector';
import TimelineContent from '@mui/lab/TimelineContent';
import TimelineDot from '@mui/lab/TimelineDot';
import TimelineOppositeContent, {
    timelineOppositeContentClasses,
  } from '@mui/lab/TimelineOppositeContent';

import "./styles/expierienceCard.css";

const ExpierienceCard = () => {
    const items = [{
        title: "May 1940",
        cardTitle: "Dunkirk",
        url: "http://www.history.com",
        cardSubtitle:"Men of the British Expeditionary Force (BEF) wade out to..",
        cardDetailedText: "Men of the British Expeditionary Force (BEF) wade out to..",
        media: {
          type: "IMAGE",
          source: {
            url: "http://someurl/image.jpg"
          }
        }
      }];


    return (<>
        <Timeline
        sx={{
            [`& .${timelineOppositeContentClasses.root}`]: {
              flex: 0.3,
            },
          }}
        >
            <TimelineItem>
                <TimelineOppositeContent color="text.secondary" className="exp-date">
                    MAR 2025 - To Date
                </TimelineOppositeContent>
                <TimelineSeparator>
                    <TimelineDot variant="outlined" />
                    <TimelineConnector />
                </TimelineSeparator>
                <TimelineContent className="exp-description">
                    <ul>
                        <li>
                            Joined Geico's Cluster Management team, where I collaborate closely on strategic cluster management and migration initiatives.
                        </li>
                        <li>
                            My responsibilities include optimizing infrastructure resources and implementing cost-effective solutions that significantly reduce operational expenses.
                        </li>
                        <li>
                            By streamlining cluster operations and applying innovative migration strategies, I help the organization maintain robust systems while achieving substantial cost savings and operational efficiencies.
                        </li>
                        {/* <li>
                            Improved the maintainability of the project by implementing and improving exception handling and collection APIs. Involved in sprint planning for the estimation of efforts for user stories and bugs.
                        </li>
                        <li>
                            Developed and executed comprehensive test cases using JUnit and Mockito, enhancing code coverage to over 90%, significantly improving code quality and reducing post-deployment issues by over 40%.
                        </li>
                        <li>
                            Produced over 10+ complex Splunk queries to generate detailed, actionable reports from log data, providing critical insights that directly influenced strategic business decisions and significantly enhanced operational efficiencies.
                        </li> */}
                    </ul>
                </TimelineContent>
            </TimelineItem>
            <TimelineItem>
                <TimelineOppositeContent color="text.secondary" className="exp-date">
                    APR 2023 - Feb 2025
                </TimelineOppositeContent>
                <TimelineSeparator>
                    <TimelineDot color="success" />
                    <TimelineConnector />
                </TimelineSeparator>
                <TimelineContent className="exp-description">
                    <ul>
                        <li>
                            Directed a team at Adept Consulting, overseeing development and deployment of new micro-services using Spring Boot and Java, orchestrating team efforts to enhance system architecture and scalability.
                        </li>
                        <li>
                            Actively involved in all SDLC phases, improving stages from requirements to coding. Optimized and tested Spring applications, increasing efficiency by 20% and reducing bugs by 35%.
                        </li>
                        <li>
                            Developed REST-based microservices using Spring Boot and Spring Data with JPA, enhancing a Maven-based build process for continuous integration with Jenkins, and improving deployment workflows.
                        </li>
                        <li>
                            Improved the maintainability of the project by implementing and improving exception handling and collection APIs. Involved in sprint planning for the estimation of efforts for user stories and bugs.
                        </li>
                        <li>
                            Developed and executed comprehensive test cases using JUnit and Mockito, enhancing code coverage to over 90%, significantly improving code quality and reducing post-deployment issues by over 40%.
                        </li>
                        <li>
                            Produced over 10+ complex Splunk queries to generate detailed, actionable reports from log data, providing critical insights that directly influenced strategic business decisions and significantly enhanced operational efficiencies.
                        </li>
                    </ul>
                </TimelineContent>
            </TimelineItem>
            <TimelineItem>
                <TimelineOppositeContent color="text.secondary" className="exp-date">
                    JUN 2022 - AUG 2022
                </TimelineOppositeContent>
                <TimelineSeparator>
                    <TimelineDot color="success" />
                    <TimelineConnector />
                </TimelineSeparator>
                <TimelineContent className="exp-description">
                    <ul>
                        <li>
                            Architected and refined 15+ RESTful APIs using Spring Boot, improving system communication and scalability; conducted 200+ API tests with Postman and documented APIs with Swagger.
                        </li>
                        <li>
                            ctively participated in agile sprints, contributing to daily scrums and sprint planning, and developed 50+ unit tests using JUnit and Mockito, achieving 95% code coverage and reducing post-deployment bugs by 30%.
                        </li>
                        <li>
                            Conducted thorough code reviews and debugging, effectively resolving issues to maintain high code quality and reducing post-deployment problems by 75%.
                        </li>
                    </ul>
                </TimelineContent>
            </TimelineItem>
            <TimelineItem>
                <TimelineOppositeContent color="text.secondary" className="exp-date">
                    JUN 2018 - DEC 2020
                </TimelineOppositeContent>
                <TimelineSeparator>
                    <TimelineDot color="success" />
                    <TimelineConnector />
                </TimelineSeparator>
                <TimelineContent className="exp-description">
                    <ul>
                        <li>
                            Rapidly ascended to a critical leadership role at Thingks Infomatics, overseeing major enhancements to two key pages and leading advancements in Computer Vision, Machine Learning, substantially boosting technological progress.
                        </li>
                        <li>
                            Created a Selenium-based automation script for UI testing, reducing effort by 40% and increasing test efficiency.
                        </li>
                        <li>
                            Designed and implemented over 20 reusable functional components using Hooks, enhancing code maintainability. 
                        </li>
                        <li>
                            Achieved a 30% reduction in load times across various web browsers, by enhancing the load times of dependencies.
                        </li>
                        <li>
                            Enhanced component optimization for maximum performance across a wide range of web-capable devices and browsers, leading to a 30% increase in user engagement and a 10% boost in revenue.
                        </li>
                        <li>
                            Spearheaded a team in developing a ML model, attaining over 90% accuracy in predicting future insurance premiums.
                        </li>
                    </ul>
                </TimelineContent>
            </TimelineItem>
            {/* <TimelineItem>
                <TimelineOppositeContent color="text.secondary">
                    9:00 am
                </TimelineOppositeContent>
                <TimelineSeparator>
                    <TimelineDot />
                    <TimelineConnector />
                </TimelineSeparator>
                <TimelineContent>Repeat</TimelineContent>
            </TimelineItem> */}
        </Timeline>
    </>);
}

export default ExpierienceCard;