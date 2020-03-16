FROM python:alpine

RUN apk add mysql mysql-client mariadb-dev --no-cache
# install dependencies
RUN pip install --upgrade pip

RUN pip install gunicorn django pandas mysqlclient

RUN git clone git@github.com:ACAA06/software /app

WORKDIR /app

CMD ["gunicorn untitled.wsgi"]