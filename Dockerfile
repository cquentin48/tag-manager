FROM python:latest

WORKDIR /cli

COPY ./ /cli/

RUN make install