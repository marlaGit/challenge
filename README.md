Introduction
============

This document will guide you through the app.

Installation
============

1. clone the repository :

`git clone https://maria_carla@bitbucket.org/maria_carla/challenge.git`

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
  
