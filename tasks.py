from celery import Celery

app = Celery('tasks',broker='pyamqp://quest@localhost//')

@app.task
def add(x,y):
    return x+y