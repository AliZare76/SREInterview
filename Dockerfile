FROM python:3.8.15-alpine

WORKDIR /app


COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY . .

RUN chmod +x ./entrypoint.sh ./celery-entrypoint.sh

EXPOSE 3000