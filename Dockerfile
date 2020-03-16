FROM python:buster

RUN apt update && apt install mariadb-client libmariadbclient-dev gcc build-essential -y
# install dependencies
RUN pip install --upgrade pip

RUN pip install gunicorn django pandas mysqlclient

RUN git clone git@github.com:ACAA06/software /app

WORKDIR /app

CMD ["gunicorn untitled.wsgi"]