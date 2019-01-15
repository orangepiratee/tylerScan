#!/usr/bin/env python

from tasks import *

for i in range(120,125):
    #add.delay(i,i)
    #multiply.delay(i,i)
    ip = '1.1.{}.0/24'.format(i)
    portScan.delay('554',ip)