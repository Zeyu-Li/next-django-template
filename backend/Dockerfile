#---- Base python ----
FROM python:3.8-slim as base

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED 1

# Create app directory
WORKDIR /src

COPY backend/requirements.txt /src

RUN pip3 install -r requirements.txt

COPY ./backend /src

EXPOSE 8000