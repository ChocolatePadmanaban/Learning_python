# sleep in python 

import os
import time
pid = os.fork()

# Fork - replicates the process So prints two Hello world
if pid==0:
    time.sleep(5)
    print("i am child, my parents pid is ", os.getppid())#get parents pid but because of 
    #sleep it becomes orpan and gets a new parent
    print("i am child, my pid is", os.getpid())
    
else:
    #os.wait()#wait forces the parent to wait
    print("Hello World from parent my pid id is", os.getpid())#get its own pid
    print("Child pid is", pid)# fork returns the process id of the child in pid