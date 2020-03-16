FROM python:buster

RUN apt update && apt install mariadb-client libmariadbclient-dev gcc build-essential openssh-client openssh-server git sudo curl wget -y
# install dependencies
RUN pip install --upgrade pip

RUN pip install gunicorn django pandas mysqlclient

# Use my generic key from host
COPY /home/ubuntu/.ssh/id_ed25519 /root/.ssh/id_ed25519
RUN chmod 600 /root/.ssh/id_ed25519

RUN git clone git@github.com:ACAA06/software /app

WORKDIR /app

CMD ["gunicorn untitled.wsgi"]