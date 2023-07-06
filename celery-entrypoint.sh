#!/bin/sh

until cd /app
do
    echo "Waiting for server volume..."
done

celery -A core worker