FROM mariadb:latest
# FROM python:3.7

ENV MYSQL_ROOT_PASSWORD test
ENV MYSQL_DATABASE Pronondb

COPY ./src/data/create_db.sql /docker-entrypoint-initdb.d/

# WORKDIR /code
#
# COPY requirements.txt .
#
# RUN pip install -r requirements.txt
#
# COPY src/ .
#
# CMD [ "python", "./main.py" ]
