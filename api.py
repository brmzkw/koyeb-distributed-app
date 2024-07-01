import random
from flask import Flask

from worker import celery_app, process_file, RABBITMQ_PASSWORD, RABBITMQ_USER, RABBITMQ_HOST


flask_app = Flask(__name__)

@flask_app.route('/')
def root():
    n = random.randrange(1, 10)
    process_file.delay(n)
    return f'Sent task to worker which will take {n} seconds to complete!'


if __name__ == "__main__":
    flask_app.run()