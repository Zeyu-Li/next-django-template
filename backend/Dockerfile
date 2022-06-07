#---- Base python ----
FROM python:3.8-slim as base

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create app directory
WORKDIR /src
COPY ./backend /src

RUN pip3 install --no-cache-dir -r requirements.txt 