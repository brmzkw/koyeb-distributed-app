import time
from celery import Celery

app = Celery('tasks', broker='pyamqp://xxx:xxx@localhost//')

@app.task
def process_file(t):
    print(f'Receiving task, sleeping for {t} seconds')
    time.sleep(t)
    print('Task completed!')