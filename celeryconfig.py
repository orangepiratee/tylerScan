#!/usr/bin/env python
#broker use rabbitmq
CELERY_BROKER_URL = 'amqp://admin:admin@localhost:5672/myvhost'
#backend use redis
CELERY_BACKEND_URL = 'redis://localhost:6379/0'
#use json
CELERY_RESULT_SERIALIZER = 'json'
#task result expires
CELERY_TASK_RESULT_EXPIRES = 60*60*24

