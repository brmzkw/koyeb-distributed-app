koyeb app create distributed-app
koyeb service create distributed-app/rabbitmq --docker rabbitmq:management --port 15672 --env RABBITMQ_DEFAULT_USER=xxx --env RABBITMQ_DEFAULT_PASS=xxx
