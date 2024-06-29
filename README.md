## Deploy on Koyeb

```
koyeb app create distributed-app

koyeb service create distributed-app/rabbitmq --docker rabbitmq:management --port 15672 --port 5672:tcp --env RABBITMQ_DEFAULT_USER=xxx --env RABBITMQ_DEFAULT_PASS=xxx

koyeb service create distributed-app/api --git github.com/brmzkw/koyeb-distributed-app --port 8000 --env RABBITMQ_HOST=rabbitmq.distributed-app.koyeb

koyeb service create distributed-app/worker --git github.com/brmzkw/koyeb-distributed-app --env RABBITMQ_HOST=rabbitmq.distributed-app.koyeb --git-buildpack-run-command 'celery -A worker worker --loglevel=INFO' --type worker
```


## Locally

* Run RabbitMQ:

```bash
docker run --rm -ti -p 5672:5672 -p 15672:15672 --env RABBITMQ_DEFAULT_USER=xxx --env RABBITMQ_DEFAULT_PASS=xxx rabbitmq:management
```

* Create virtualenv

```bash
virtualenv venv
pip install -vr requirements.txt
```

* Start the API

```bash
source ./venv/bin/activate
FLASK_DEBUG=t python api.py
```

* Start the worker

```bash
source ./venv/bin/activate
celery -A worker worker --loglevel=INFO
```