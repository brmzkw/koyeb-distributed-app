import os
import time
from celery import Celery
from kombu import Exchange, Queue
import pika

from sdk.openapi_client import ApiClient, Configuration, ServicesApi

RABBITMQ_USER = os.getenv('RABBITMQ_USER', 'xxx')
RABBITMQ_PASSWORD = os.getenv('RABBITMQ_PASS', 'xxx')
RABBITMQ_HOST = os.getenv('RABBITMQ_HOST', 'localhost')
KOYEB_API_KEY = os.environ.get('KOYEB_API_KEY')

celery_app = Celery('tasks', broker=f'pyamqp://{RABBITMQ_USER}:{RABBITMQ_PASSWORD}@{RABBITMQ_HOST}//')

celery_app.conf.task_acks_late = True
celery_app.conf.worker_prefetch_multiplier = 1

celery_app.conf.task_queues = [
    Queue('high_priority', Exchange('high_priority'), routing_key='high_priority', queue_arguments={'x-max-priority': 10}),
]

# Use the high_priority queue for the scale_koyeb_service task. If the main
# queue is overloaded, the scale_koyeb_service should still be able to run.
celery_app.conf.task_routes = ([
    ('worker.scale_koyeb_service', {'queue': 'high_priority'}),
],)


@celery_app.task(priority=1)
def process_file(t):
    print(f'Receiving task, sleeping for {t} seconds')
    time.sleep(t)
    print('Task completed!')


@celery_app.task(priority=0)
def scale_koyeb_service():
    credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASSWORD)
    connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_HOST, credentials=credentials))
    channel = connection.channel()
    queue = channel.queue_declare(queue='celery', passive=True)
    ready_tasks = queue.method.message_count
    print('>>>> READY TASKS=', ready_tasks)

    configuration = Configuration(
        host="https://app.koyeb.com",
        api_key={
            'Bearer': KOYEB_API_KEY,
        },
        api_key_prefix={
            'Bearer': 'Bearer'
        }
    )

    with ApiClient(configuration) as api_client:
        services = ServicesApi(api_client).list_services()
        print('>>>>>', services)


@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Executes every 3 seconds
    sender.add_periodic_task(10.0, scale_koyeb_service.s(), name='Scale Koyeb service')