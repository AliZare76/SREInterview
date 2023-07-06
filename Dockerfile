FROM python:3.8.15-alpine
# RUN apt-get update && apt install python3-dev gcc libc-dev

WORKDIR /app


COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY . .

RUN chmod +x ./entrypoint.sh ./celery-entrypoint.sh
