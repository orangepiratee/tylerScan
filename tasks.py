from __future__ import absolute_import, unicode_literals
from tylerscope import app
import os

@app.task
def add(x,y):
    return x+y

@app.task
def multiply(x,y):
    return x*y

@app.task
def xsum(numbers):
    return sum(numbers)

@app.task
def signup():
    print('i am here now.')

@app.task
def portScan(port='554',ip='1.1.110.0/24'):
    try:
        if not os.path.exists(os.getcwd()+'/data'):
            os.popen('mkdir data')
        fname = 'data/{}_{}.txt'.format(port, ip.replace('.', '_').replace('/', '_'))
        command = 'zmap -B 10M -p {} {} -o {}'.format(port,ip,fname)
        text = os.popen(command)
        return 0
    except:
        return 1
    #save2txt(text,fname)