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
KOYEB_API_KEY = os.environ.get('KOYEB_API_KEY')

KOYEB_WORKER_APP = os.getenv('KOYEB_WORKER_APP', 'dapp-worker')
KOYEB_WORKER_SERVICE = os.getenv('KOYEB_WORKER_SERVICE', 'worker')

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
    print('Checking if we need to scale the service')

    # Connect to RabbitMQ, and get the number of tasks in the default "celery" queue used to process tasks.
    credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASSWORD)
    connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_HOST, credentials=credentials))
    channel = connection.channel()
    queue = channel.queue_declare(queue='celery', passive=True)
    ready_tasks = queue.method.message_count

    # Let's assume we want to have maximum 10 tasks in the queue per worker
    expected_count = math.ceil(ready_tasks / 10)
    print(f'Queue has {ready_tasks} tasks, expected workers count: {expected_count}')

    # Perform the scaling if needed
    do_service_scale(expected_count)


def do_service_scale(expected_count):
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
        # Retrieve Koyeb application
        apps = AppsApi(api_client).list_apps(name=KOYEB_WORKER_APP).apps
        if len(apps) != 1:
            raise ValueError(f'Expected 1 app with name {KOYEB_WORKER_APP}, got {len(apps)}')

        # Retrieve Koyeb service
        services = ServicesApi(api_client).list_services(app_id=apps[0].id, name=KOYEB_WORKER_SERVICE).services
        if len(services) != 1:
            raise ValueError(f'Expected 1 service with name {KOYEB_WORKER_SERVICE}, got {len(services)}')

        # Get the current deployment
        latest_deployment_id = services[0].latest_deployment_id
        deployment = DeploymentsApi(api_client).get_deployment(id=latest_deployment_id).deployment

        # Assuming we have only one scaling group, and all the scaling groups have the same min/max values
        current_count = deployment.definition.scalings[0].min

        if current_count == expected_count:
            print(f'Service already scaled to {expected_count} instances, skipping')
            return
        elif current_count > expected_count:
            direction = 'down'
            new_count = current_count - 1
        else:
            direction = 'up'
            new_count = current_count + 1

        # Force to have at least 1 worker
        if new_count < 1:
            new_count = 1

        for idx, _ in enumerate(deployment.definition.scalings):
            deployment.definition.scalings[idx].min = new_count
            deployment.definition.scalings[idx].max = new_count

        update_body = UpdateService(definition=deployment.definition, skip_build=True)
        ServicesApi(api_client=api_client).update_service(
            id=services[0].id,
            service=update_body
        )
        print(f'Scaling {direction} service to {new_count} instances')


@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Executes every 10 seconds
    sender.add_periodic_task(60.0, scale_koyeb_service.s(), name='Scale Koyeb service')