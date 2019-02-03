# Accessing SSH from python and trasnsferring file
import os
import paramiko

def printTotals(transferred, toBeTransferred):
    print("Transferred: {0}\tOut of: {1}".format(transferred,toBeTransferred))

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='127.0.0.1', username="cisco",
password="cisco", port="22")
sftp= ssh.open_sftp()
localpath = 'hello.py'
remotepath = '/tmp/urname.py'
sftp.put(localpath, remotepath,callback=printTotals)
sftp.close()
ssh.close()