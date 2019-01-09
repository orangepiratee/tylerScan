import time
from celery import Celery

brokerUrl = 'amqp://admin:admin@localhost:5672/myvhost'
backendUrl = 'amqp://127.0.0.1:15672'

app = Celery('tasks',broker=brokerUrl)

@app.task
def add(x,y):
    print('sleep 2 seconds...')
    time.sleep(2)
    return x+y