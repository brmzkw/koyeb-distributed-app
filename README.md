```
koyeb app create distributed-app
koyeb service create distributed-app/rabbitmq --docker rabbitmq:management --port 15672 --env RABBITMQ_DEFAULT_USER=xxx --env RABBITMQ_DEFAULT_PASS=xxx

koyeb service create distributed-app/api --git github.com/brmzkw/koyeb-distributed-app --port 8000 --env RABBITMQ_HOST=rabbitmq.distributed-app.koyeb

koyeb service create distributed-app/worker --git github.com/brmzkw/koyeb-distributed-app --env RABBITMQ_HOST=rabbitmq.distributed-app.koyeb --git-buildpack-run-command 'celery -A worker worker --loglevel=INFO' --type worker
```
