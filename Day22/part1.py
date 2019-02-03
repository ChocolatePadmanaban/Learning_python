# Execute some system commands with wait time 1 hour
import os

import time
def time_cycle(wait_time= 3600):
    for i in range(10):
        print(os.system('ls'))
        time.sleep(wait_time)

if __name__ == '__main__':
    time_cycle(3)