import atexit
import datetime
import math
import os
import random

from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask
import pika

from sdk.openapi_client import ApiClient, Configuration, ServicesApi, AppsApi, DeploymentsApi, UpdateService

from worker import process_file, RABBITMQ_PASSWORD, RABBITMQ_USER, RABBITMQ_HOST



flask_app = Flask(__name__)

KOYEB_API_KEY = os.environ.get('KOYEB_API_KEY')
KOYEB_WORKER_APP = os.getenv('KOYEB_WORKER_APP', 'dapp-worker')
KOYEB_WORKER_SERVICE = os.getenv('KOYEB_WORKER_SERVICE', 'worker')

last_scale_event = None

def scale_app():
    global last_scale_event
    if last_scale_event:
        if datetime.datetime.now() - last_scale_event < datetime.timedelta(minutes=5):
            print('We scaled the service recently, avoid to scale again')
            return
    
    print('Checking if we need to scale the service...')

    # Connect to RabbitMQ, and get the number of tasks in the default "celery" queue used to process tasks.
    credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASSWORD)
    connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_HOST, credentials=credentials))
    channel = connection.channel()
    queue = channel.queue_declare(queue='celery', passive=True)
    ready_tasks = queue.method.message_count

    # Let's assume we want to have maximum 50 tasks in the queue per worker, with a minimum of 1 worker
    expected_count = max(math.ceil(ready_tasks / 10), 1)
    print(f'>> Queue has {ready_tasks} tasks, expected workers count: {expected_count}')

    # Perform the scaling if needed
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

        # Here, we assume the service is deployed with the same scaling policy everywhere
        current_count = deployment.definition.scalings[0].min

        if current_count == expected_count:
            print(f'>> Service already scaled to {expected_count} instances, skipping')
            return

        if current_count > expected_count:
            new_count = current_count - 1
            print(f'Scaling down service from {current_count} to {new_count} instances')
        else:
            new_count = current_count + 1
            print(f'Scaling up service from {current_count} to {new_count} instances')

        for idx, _ in enumerate(deployment.definition.scalings):
            deployment.definition.scalings[idx].min = new_count
            deployment.definition.scalings[idx].max = new_count

        update_body = UpdateService(definition=deployment.definition, skip_build=True)
        ServicesApi(api_client=api_client).update_service(
            id=services[0].id,
            service=update_body
        )
        last_scale_event = datetime.datetime.now()


@flask_app.route('/')
def root():
    n = random.randrange(1, 10)
    process_file.delay(n)
    return f'Sent task to worker which will take {n} seconds to complete!'


def create_app():
    # In debug mode, Flask will reload itself on code changes. Avoid setting up the scheduler in this case.
    if not flask_app.debug or os.environ.get("WERKZEUG_RUN_MAIN"):
        scheduler = BackgroundScheduler()
        scheduler.add_job(func=scale_app, trigger="interval", seconds=10)
        scheduler.start()
        # Shut down the scheduler when exiting the app
        atexit.register(lambda: scheduler.shutdown())
    return flask_app


def debug():
    app = create_app()
    app.run()


if __name__ == "__main__":
    debug()