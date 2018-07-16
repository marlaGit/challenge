Introduction
============

This document will guide you through the app.


Challenge
=========

`The goal is to create a simple web application using a modern web development framework.`
 
`In particular, using RESTful APIs and a mobile-first approach, that allows users to fill in a questionnaire and receive graphical feedback in return.

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


Installation
============

1. clone the repository :

`git clone https://github.com/marlaGit/challenge`

2. enter into the directory:

`cd challenge` 

3. run the project:

`docker-compose up`

At the first try, the database container might take to long to run and web container might crash. If that so, wait for the
database container to be started, stop both containers with Ctrl+C, and re-run 

`docker-compose up`

Admin interface
=====

While the server running, open http://0.0.0.0:8000/ with your browser. Log as superuser 
(username is `root` and password `root@challenge`).

- If logged as superuser you will be redirect automatically to 
admin page. From the admin page it is possible to create questionnaires,
questions and see user results and information.  

- To create a questionnaire. On the right of "questionnaires", 
click on '+ Add'. You must fill both the title and the leanings.
Leanings are the tendencies of the answers and have no limit in number.
For a politic questionnaire for example, leanings could be set
as left and right.

- To create/add questions. Once created the questionnaire, you will
be redirected to the list of the existing questionnaires. From here
it is possible to create a new question using the link `New question`
under the section CREATE QUESTION or visualize/modify the existing 
questions associated to each questionnaire by clicking on the 
text of the question.
When creating a new question the questionnaire and the leanings 
associated are automatically loaded.

- To see the information on the users who answered to the questionnaires 
click on User choices. This section includes all the information
 on the answer of each user and all the information on the user browser,
 device, location, IP address etc..

- Superuser can modify permissions of each user.
 
Web interface
=====

 While the server running, open http://0.0.0.0:8000/ with your browser. Log as username `user1` and password `1234` 
 or click on new user button to create a new user (of course 
 each created user will not have access to the admin interface).
 Once logged, user is redirected to the list of questionnaires. User can start a questionnaire by clicking on it. 
 One question per page is displayed, to optimize the mobile interface. User can choose only one answer per question and click on next 
 to see the next question. At the end of the questionnaire the user is redirected to the result page with a pie chart 
 displayed. User can change his answer by refilling the questionnaire (his previous answers are selected by default).
 
REST API
====

A REST API (configured as JSON) has been implemented and it is available to the superuser. Schema of the API is 
available at 

`http -a root:root@challenge http://0.0.0.0:8000/schema/` 

For example to get all the answers:

`http -a root:root@challenge http://0.0.0.0:8000/userchoices/`
  
