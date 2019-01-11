#!/usr/bin/env python
#broker use rabbitmq
BROKER_URL = 'amqp://admin:admin@192.168.1.17:5672/myvhost'
#backend use redis
CELERY_RESULT_BACKEND = 'redis://localhost:6379/1'
#use json
CELERY_RESULT_SERIALIZER = 'json'
#task result expires
CELERY_TASK_RESULT_EXPIRES = 60*60*24
#task child dead after 40 times processing
CELERY_MAX_TASKS_PER_CHILD = 40

CELERY_QUEUES = (


)

