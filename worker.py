import os
import time
from celery import Celery

RABBITMQ_USER = os.getenv('RABBITMQ_USER', 'xxx')
RABBITMQ_PASSWORD = os.getenv('RABBITMQ_PASS', 'xxx')
RABBITMQ_HOST = os.getenv('RABBITMQ_HOST', 'localhost')

celery_app = Celery('tasks', broker=f'pyamqp://{RABBITMQ_USER}:{RABBITMQ_PASSWORD}@{RABBITMQ_HOST}//')

@celery_app.task
def process_file(t):
    print(f'Receiving task, sleeping for {t} seconds')
    time.sleep(t)
    print('Task completed!')