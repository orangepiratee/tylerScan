#!/usr/bin/env python
from __future__ import absolute_import, unicode_literals
from celery import Celery
import sys,os
import time

sys.path.append(os.path.abspath("."))

app = Celery('tylerscope',include=['tasks'])
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

infoo()
#if __name__ == '__main__':
#    app.start()
