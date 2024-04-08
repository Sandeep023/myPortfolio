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
                    APR 2023 - To Date
                </TimelineOppositeContent>
                <TimelineSeparator>
                    <TimelineDot variant="outlined" />
                    <TimelineConnector />
                </TimelineSeparator>
                <TimelineContent className="exp-description">
                    I have been deeply involved in every stage of the Software Development Life Cycle 
                    (SDLC), focusing on performance optimization and comprehensive testing of Spring applications. 
                    He successfully led the redesign and development of a new user interface, 
                    enhancing user experience by 25% and improving database operations across multiple platforms to 
                    ensure data integrity. Additionally, Sandeep architected and implemented REST-based Microservices 
                    using Spring Boot and Spring Data with JPA, significantly contributing to a Maven-based build
                     process that supports continuous integration with Jenkins, thus streamlining deployment 
                     and development workflows.
                </TimelineContent>
            </TimelineItem>
            <TimelineItem>
                <TimelineOppositeContent color="text.secondary" className="exp-date">
                    JUN 2023 - AUG 2023
                </TimelineOppositeContent>
                <TimelineSeparator>
                    <TimelineDot color="success" />
                    <TimelineConnector />
                </TimelineSeparator>
                <TimelineContent className="exp-description">
                    I have engineered and maintained high-performance, responsive full-stack web 
                    applications utilizing ReactJS and Java/Spring Boot, enhancing user experience through best practices 
                    in UI/UX design across various platforms. He has significantly improved system interoperability by 
                    spearheading the integration of RESTful APIs and SOAP services, facilitating seamless communication 
                    between front-end and back-end systems. Additionally, Sandeep has been pivotal in ensuring 
                    exceptional code quality by leading thorough code reviews and debugging processes, 
                    swiftly identifying and resolving issues.
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
                    I have been an integral leader in the Agile development process, skillfully leading a team 
                    of five junior developers through sprint planning, daily stand-ups, and retrospectives, 
                    ensuring best practices and mentorship. He has significantly enhanced software development 
                    efficiencies by designing over 20 reusable React Hook components, integrating RESTful APIs, 
                    and employing Redux for improved state management, which collectively cut development time by 
                    25% and reduced system load times by 30%, boosting user engagement by 30% and increasing revenue by 
                    10%. Additionally, Sandeep has pioneered a sophisticated machine learning model to predict insurance 
                    premiums with over 90% accuracy and developed a Selenium-based UI testing script that reduced manual 
                    effort by 40%, greatly increasing test efficiency.
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