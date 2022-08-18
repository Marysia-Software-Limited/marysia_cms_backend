# syntax=docker/dockerfile:1
FROM python:3.10
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -Ur requirements.txt
COPY . /code/
RUN manage.py createdb
RUN manage.py createsuperuser --noinput
