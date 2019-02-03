# unix alarm using python


import signal
import time
def alarm_handler(signalnum, stack):
    print("Alarm raised", time.ctime())

signal.signal(signal.SIGALRM, alarm_handler)
signal.alarm(4)
print("Current time:", time.ctime())
time.sleep(6)