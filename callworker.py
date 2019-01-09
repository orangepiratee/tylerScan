from tasks import add
from celery import Celery

add.delay(3,4)
add.delay(4,4)