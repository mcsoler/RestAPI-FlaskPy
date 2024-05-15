#!/usr/bin/python

from GProcess import GProcess
import time
import os
import yaml

config_file = sys.argv[1]
f = open(config_file,'r')
srvs = yaml.safe_load(f)

c=0
proc = GProcess()
while True:
    for srv_nam,srv in srvs['procs'].items():
        if not proc.is_running([srv_nam]):
            try:
                print("Proc "+ srv_nam + " is not running, starting it ")
                os.system(srv['save_log'])
                os.system(srv['stop'])
                time.sleep(1)
                os.system(srv['start'])
            except:
                pass
        else:
            pass
            #print("Proc "+ srv + " is running")
    if c > 10:
        break
    c += 1
    time.sleep(5)
