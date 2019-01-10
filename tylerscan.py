#!/usr/bin/env python
from __future__ import absolute_import
from celery import Celery

brokerUrl = 'amqp://administrator:admin@localhost:5672/myvhost'
backendUrl = 'redis://localhost:6379'
app = Celery('pj',broker=brokerUrl,backend=backendUrl,include=['tylerScan.tasks'])

app.config_from_object('tylerScan.celeryConfig')

if