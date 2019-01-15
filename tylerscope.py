#!/usr/bin/env python
from __future__ import absolute_import, unicode_literals
from celery import Celery, platforms
import sys,os
import time

platforms.C_FORCE_ROOT = True

sys.path.append(os.path.abspath("."))

app = Celery('tasks',include=['tasks'])
app.config_from_object('celeryconfig')

def my_decorator(func):
    def wrapper():
        print('before the func runs')
        func()
        print('after the func runs')
    return wrapper

@my_decorator
def infoo():
    print('nh.....')

if __name__ == '__main__':
    app.start()
