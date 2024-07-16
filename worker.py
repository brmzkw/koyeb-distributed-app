import math
import os
import time
from celery import Celery
from kombu import Exchange, Queue
import pika

from sdk.openapi_client import ApiClient, Configuration, ServicesApi, AppsApi, DeploymentsApi, UpdateService

RABBITMQ_USER = os.getenv('RABBITMQ_USER', 'xxx')
RABBITMQ_PASSWORD = os.getenv('RABBITMQ_PASS', 'xxx')
RABBITMQ_HOST = os.getenv('RABBITMQ_HOST', 'localhost')


celery_app = Celery('tasks', broker=f'pyamqp://{RABBITMQ_USER}:{RABBITMQ_PASSWORD}@{RABBITMQ_HOST}//')
celery_app.conf.task_acks_late = True
celery_app.conf.worker_prefetch_multiplier = 1


@celery_app.task(priority=1)
def process_file(t):
    print(f'Receiving task, sleeping for {t} seconds')
    time.sleep(t)
    print('Task completed!')