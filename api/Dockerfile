FROM python:3.9-slim AS build

ENV DB_HOST=http://localhost:3306 DB_USER=flask-application

WORKDIR /code

COPY requirements.txt .

RUN --mount=type=cache,target=/root/.cache/pip pip install -r requirements.txt

ARG AIOHTTP_VERSION=3.12.13 REQUESTS_VERSION

FROM python:3.9-slim AS dev

COPY --from=build /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY --from=python:3.10-slim /usr/local/bin/python /usr/local/bin/python3.10
COPY --from=bash:4.4 /usr/local/bin/bash /usr/local/bin/bash


FROM python:3.9-alpine AS prod

COPY --from=build /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages

WORKDIR /code

COPY . .

EXPOSE 5000

CMD ["python3", "main.py"]
