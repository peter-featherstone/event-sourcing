FROM python:3.7-alpine

RUN pip install --upgrade pip

ADD ./requirements.txt /requirements.txt

# Runtime dependencies
RUN apk update && apk add libpq

# Build dependencies
RUN apk add --no-cache --virtual .build-deps \
    postgresql-dev gcc musl-dev && \
    pip install -r /requirements.txt && \
    apk --purge del .build-deps && rm requirements.txt

ADD ./service /service

WORKDIR /service
ENV PYTHONPATH /
