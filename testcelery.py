#!/usr/bin/env python

from tasks import *

for i in range(100,121):
    #add.delay(i,i)
    #multiply.delay(i,i)
    ip = '1.1.{}.0/24'.format(i)
    portScan.delay('80',ip)