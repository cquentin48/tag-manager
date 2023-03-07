FROM python:latest

WORKDIR /app

COPY ./ /app/

RUN make install