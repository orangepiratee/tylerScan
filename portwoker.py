import os
import datetime

def portScan(port='554',ip='1.1.110.0/24'):
    if not os.path.exists(os.getcwd()+'/data'):
        os.popen('mkdir data')
    current_time = datetime.datetime
    os.times()
    fname = 'data/{}_{}.txt'.format(port, ip.replace('.', '_').replace('/', '_'))
    command = 'zmap -B 10M -p {} {} -o {}'.format(port,ip,fname)
    text = os.popen(command)
    #save2txt(text,fname)

