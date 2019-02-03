# child notes the file to be deleted 
# parent delet the files noted


import os
import time
pid = os.fork()

# Fork - replicates the process So prints two Hello world
if pid==0:
    print("i am child, my parents pid is ", os.getppid())#get parents pid but because of 
    #sleep it becomes orpan and gets a new parent
    print("i am child, my pid is", os.getpid())
    l = os.listdir("check")
    f= open('abc.txt','w')
    for i in l:
        statinfo = os.stat('check/'+i)
        f.write(i+' '+str(statinfo.st_size)+'\n')
    f.close()

else:
    os.wait()#wait forces the parent to wait
    print("Hello World from parent my pid id is", os.getpid())#get its own pid
    print("Child pid is", pid)# fork returns the process id of the child in pid
    f = open('abc.txt')
    l = f.readlines()
    l =[i.strip().split(' ') for i in l]
    to_delete = []
    for i in range(len(l)):
        if int(l[i][1]) == 0:
            to_delete.append(l[i][0])
    for i in to_delete:
        os.remove('check/'+i)
        