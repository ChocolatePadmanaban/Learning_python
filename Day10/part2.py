from tqdm import tqdm
import sys
import time
import paramiko
def viewBar(a,b):
    res = a/int(b)*100
    sys.stdout.write('\rComplete precent: %.2f %%'%(res))
    sys.stdout.flush()
def viewBar2(a,b):
    pbar = tqdm(total=int(b), ascii=True,unit='b',unit_scale=True)
    pbar.update(a)
    
t= paramiko.Transport(('127.0.0.1',22))
t.connect(username='cisco',password='cisco')

sftp = paramiko.SFTPClient.from_transport(t)
sftp.put('progit.pdf', '/tmp/did.pdf', callback= viewBar)
