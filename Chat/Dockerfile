FROM python:3.9-alpine

WORKDIR /usr/scr/app

RUN apk update && apk add ca-certificates build-base mariadb-client mariadb-dev
RUN pip install --upgrade pip
RUN pip install flask flask-sqlalchemy mysqlclient flask-migrate
COPY chat.py ./
COPY migrations ./migrations
CMD ["python", "chat.py"]
EXPOSE 5000