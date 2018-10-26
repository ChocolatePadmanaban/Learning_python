# Sockets used to get data from 

import  socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("www.google.com", 80))#connect
s.send(b"GET /index.html HTTP/1.0\n\n")#Send request
data = s.recv(100000)
print(data)
s.close()