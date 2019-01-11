#!/usr/bin/env python

from tasks import *

for i in range(50):
    add.delay(i,i)
    mul.delay(i,i)