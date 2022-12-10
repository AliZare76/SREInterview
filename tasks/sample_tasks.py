import time

from celery import shared_task


@shared_task
def create_task(duration):
    time.sleep(int(duration))
    return True
