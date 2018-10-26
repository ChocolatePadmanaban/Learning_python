# threading example


import time
import _thread


def myfunction(string,sleeptime, lock, *args):
    while 1:
        #entering critical section
        lock.acquire()
        print(string,"Now sleeping lock is acquired") 
        time.sleep(sleeptime)
        print(string,"now releasing lock and sleeping again")         
        lock.release()
        time.sleep(sleeptime)



if __name__ =="__main__":
    lock = _thread.allocate_lock()
    _thread.start_new_thread(myfunction,('Thread No:1',2,lock))
    _thread.start_new_thread(myfunction,('Thread No:2',2,lock))

    while 1:
        pass