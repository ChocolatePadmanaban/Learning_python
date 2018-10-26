# high level threading

import threading # high level threading (low level threading -> threading)
import time

class PrintTime(threading.Thread):
    def __init__(self, timer):
        threading.Thread.__init__(self)
        self.interval = timer
    def run(self):
        while True:
            time.sleep(5)
            print(time.ctime(time.time()))

p1 = PrintTime(5)
p1.start()
while True:
    pass