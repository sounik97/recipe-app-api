FROM python:3.7-alpine
MAINTAINER SOUNIK

ENV PYTHONUNBUFFERED 1

# copy the requirements to our requirements new file

COPY ./requirements.txt ./requirements.txt

RUN pip install -r /requirements.txt

# create a directory app and copy the workdir to app folder
# (/app is default directory)

RUN mkdir /app
WORKDIR /app
COPY ./app /app

# -D represents create user for running application only not for other tasks
# 'USER user' command switches to new 'user' which we just created
# Otherwise the docker image will run using root account (not recommended)

RUN adduser -D user
USER user
