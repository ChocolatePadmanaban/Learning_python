# escaping intrepets(ctrl+c) in unix using python

import signal
import time

def handler(a,b):
    print("signal number", a, 'frame', b)
    signal.signal(signal.SIGINT,signal.SIG_DFL)# makes it do only once 

signal.signal(signal.SIGINT,handler)
while True:
    print("not afraid of C -c") # make it escape (ctrl + c)
    time.sleep(1)