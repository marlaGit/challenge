FROM python:3
 ENV PYTHONUNBUFFERED 1
 RUN mkdir /application
 WORKDIR /application
 ADD application /application/
 RUN pip install -r requirements.txt
