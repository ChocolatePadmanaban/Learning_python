# Unix using Python

import os
x= 9
pid = os.fork()

# Fork - replicates the process So prints two Hello world
if pid==0:
    print("i am child, my parents pid is ", os.getppid())#get parents pid
    print("i am child, my pid is", os.getpid())
    x = x+9 # not reflected in parent because there are 2 duplicates
    print('x is ', x)
    f= open("numberStore.txt",'w')
    f.write(str(x))
    f.close()
else:
    os.wait()#wait forces the parent to wait
    print("Hello World from parent my pid id is", os.getpid())#get its own pid
    print("Child pid is", pid)# fork returns the process id of the child in pid
    f=open("numberStore.txt")
    x=int(f.read())
    print('x is',x)
    f.close()
