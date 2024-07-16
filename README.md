## Deploy on Koyeb

```
koyeb app create dapp-rabbitmq
koyeb service create dapp-rabbitmq/rabbitmq --docker rabbitmq:management --port 15672 --port 5672:tcp --env RABBITMQ_DEFAULT_USER=xxx --env RABBITMQ_DEFAULT_PASS=xxx --route /:15672

koyeb app create dapp-api
koyeb service create dapp-api/api --git github.com/brmzkw/koyeb-distributed-app --port 8000 --env RABBITMQ_HOST=rabbitmq.dapp-rabbitmq.koyeb

koyeb app create dapp-worker
export KOYEB_API_KEY=<xxx>
koyeb service create dapp-worker/worker --git github.com/brmzkw/koyeb-distributed-app --env RABBITMQ_HOST=rabbitmq.dapp-rabbitmq.koyeb --git-buildpack-run-command 'celery -A worker worker --loglevel=INFO' --type worker --env KOYEB_API_KEY=$KOYEB_API_KEY
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
export RABBITMQ_USER=xxx
export RABBITMQ_PASS=xxx
export RABBITMQ_HOST=localhost
FLASK_DEBUG=t python api.py
```

* Start the worker

```bash
source ./venv/bin/activate
export RABBITMQ_USER=xxx
export RABBITMQ_PASS=xxx
export RABBITMQ_HOST=localhost
export KOYEB_API_KEY=<api key>
celery -A worker worker --loglevel=INFO -B
```