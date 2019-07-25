FROM python:3.7-alpine

RUN pip install --upgrade pip

ADD ./requirements.txt /requirements.txt

RUN apk update  && apk add libpq

RUN apk update && \
    apk add --no-cache --virtual .build-deps \
    postgresql-dev gcc musl-dev && \
    pip install -r /requirements.txt && \
    apk --purge del .build-deps && rm requirements.txt

ADD ./service /service
