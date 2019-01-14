#!/usr/bin/env python
from kombu import Queue
from kombu import Exchange
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
    Queue('priority_low', exchange=Exchange('priority', type='direct'), routing_key='priority_low'),
    Queue('priority_high', exchange=Exchange('priority', type='direct'), routing_key='priority_high'),
)

CELERY_ROUTES = ([
                     ('tasks.add',{'queue':'priority_low'}),
                     ('tasks.multiply',{'queue':'priority_high'}),
],)
