import time
from __future__ import absolute_import, unicode_literals
from celery import Celery

brokerUrl = 'amqp://admin:admin@localhost:5672/myvhost'
backendUrl = 'redis://127.0.0.1:6379'

app = Celery('tasks',broker=brokerUrl,backend=backendUrl)

@app.task
def add(x,y):
    print('sleep 2 seconds...')
    time.sleep(2)
    return x+y