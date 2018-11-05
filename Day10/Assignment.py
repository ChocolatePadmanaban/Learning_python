# Reading the File from ftp.gnu.org

import socket 
import sys

from ftplib import FTP
ftp = FTP('ftp.gnu.org')
ftp.login()
ftp.retrbinary('RETR README', open('README', 'wb').write)
ftp.quit()

#reading the file and getting the lines with the

f= open("README")
ListOfLines= f.readlines()
LinesWithThe =[]
for i in ListOfLines:
    if 'THE' in i.upper():
        LinesWithThe.append(i)

# Client Code
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10003)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

Wf = open("WrittenREADME.txt",'w')
writeReadME = []

for i in LinesWithThe:
    try:
        # Send data
        message = bytes(i, 'utf-8')
        #print('sending {!r}'.format(message))
        sock.sendall(message)

        # Look for the response
        amount_received = 0
        amount_expected = len(message)

        while amount_received < amount_expected:
            data = sock.recv(200)
            amount_received += len(data)
            #print('received {!r}'.format(data))
            writeReadME.append(data)
    except:
        pass

print(writeReadME)
for i in writeReadME:
    Wf.write(str(str(i, 'UTF-8'),'utf-8'))
Wf.close()
sock.close()