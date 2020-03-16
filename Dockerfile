FROM python:buster

RUN apt update && apt install mariadb-client libmariadbclient-dev gcc build-essential openssh-client openssh-server git sudo curl wget -y
# install dependencies
RUN pip install --upgrade pip

RUN pip install gunicorn django pandas mysqlclient

COPY . /app

WORKDIR /app

CMD ["gunicorn untitled.wsgi"]