#!/usr/bin/env python
from __future__ import absolute_import, unicode_literals
from celery import Celery

brokerUrl = 'amqp://admin:admin@localhost:5672/myvhost'
backendUrl = 'redis://localhost:6379'
app = Celery('pj',broker=brokerUrl,backend=backendUrl,include=['tasks'])

#app.config_from_object('pj.celeryConfig')
app.conf.update(result_expires=3600,)

if __name__ == '__main__':
    app.start()