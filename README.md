Introduction
============

This document will guide you through the tasks we expect you to complete.


Challenge
=========

The goal is to create a simple web application using a modern web development framework. In particular, using RESTful APIs and a mobile-first approach, that allows users to fill in a questionnaire and receive graphical feedback in return.

All answers should be stored in a database of your choice, together with metadata such as IP address, browsing source, and whatever additional information you are capable of extracting.

The questions and answers in the questionnaire should be dynamically generated on the server side, or using the standard features of your framework (i.e., not just static HTML). An example of the questionnaire is given below.

The users' answers on the front-end should be collected by the server and used to calculate a simple pie chart with the results. The pie chart should then be displayed to the user.

Questionnaire
=========

This questionnaire is based on the following popular infographic, that tests your political leanings in terms of "left" and "right":
http://www.dailyinfographic.com/wp-content/uploads/2012/08/leftright_US_1416.gif

You can use the following example questions and answers.

1. How would you best describe an ideal government?
- Is progressive by nature
- Is conservative by nature
- Tends to look into the future
- Tends to look into the past
- Values meritocracy
- Values egalitarianism
- Promotes free trade
- Promotes fair trade
- Focuses on the individual
- Focuses on society

2. Which traits would you pass on to your child?
- Self-reliance
- Self-nurturing
- Self-defence
- Openness
- Moral strength
- Empathy
- Self-discipline
- Self-examination

3. Would you rather vote for:
- Aggression
- Diplomacy
- Upholding order
- Fairness
- Helping those who help themselves
- Helping those who cannot help themselves
- Champions of opportunity
- Champions of the downtrodden

For simplicity, the answers are organized in alternated left/right leaning.

Your server side "calculation engine" will weight these responses and determine the user's political leanings, in terms of % left / % right, and generate a 2-slice pie chart accordingly.


Environment
===========

We have provided a docker compose file and set up a container with python3 and django for you to complete the task. If you want to use a different programming language or framework you are free to do so, but you must provide your own docker configuration.


Assessment
==========

We are looking for someone not only with experience but also self-motivated and able to develop creative solutions. We welcome thinking out of the box! This assessment is designed to challenge you, and provide an instructive and fun experience.

Extra kudos if you document your solution, either with comments on your code or in a separate documents' structure. For example, you can use sphinx to document relevant development decisions, commands, research, web links etc.

We like people who are able to learn and research. Even if you might not get the tasks completed, your notes will help us in the evaluation of your work.


Other notes
==========

- Please try and complete the assessment within one week of receiving it.
- Explain your solutions in 2-3 lines.
- Create git repository to track and share your work. Please link commits relevant to each task completed. We recommend you create a Bitbucket account and a private git repository (there's no cost to you). Invite "FelipeM_ntoya" and "odemakov" to your repository team.
- Share your results even if you don't finish.
- We understand there's more than one way to do things. If you're stuck, pick one and justify your choice.


Assumptions
===========

You know how to use docker. If you don't, a good starting point is https://docs.docker.com/get-started/.
We avoid doing any manual work when setting up or deploying services. Your solution should run by simply running `docker-compose up`.


Rules
=====

Please keep this assessment to yourself, i.e. don't share it with you colleagues, friends and the rest of the world.
Keep the repository private.
You, and you alone, are expected to be the unique author of the solutions for this assessment. You will be questioned on details of the solution you provide.


Feedback
========

Please feel free to provide any feedback you have about this the assessment or even propose any technical and not technical improvement.
