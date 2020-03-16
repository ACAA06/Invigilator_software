FROM python:alpine

RUN apk add mysql mysql-client mariadb-dev --no-cache
# install dependencies
RUN pip install --upgrade pip


#### Kanged from https://github.com/baalajimaestro/userbot_docker/blob/876d9a0b600883a05da3c219a1c436eeb40e2b5f/Dockerfile#L128
RUN apk add --no-cache --update \
      git \
      bash \
      redis \
      libpq \
      curl \
      sudo \
      neofetch \
      musl \
      libxml2 \
      libwebp-dev \
      libffi-dev \
      openssl-dev \
      musl-dev \
      gcc \
      libxslt-dev \
      libxml2-dev \
      zlib \
      zlib-dev \
      libjpeg \
      libjpeg-turbo-dev \
      linux-headers \
      jq \
      pv

RUN pip install gunicorn django pandas mysqlclient

RUN git clone git@github.com:ACAA06/software /app

WORKDIR /app

CMD ["gunicorn untitled.wsgi"]