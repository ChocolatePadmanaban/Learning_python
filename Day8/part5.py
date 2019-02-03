# UDP client code

import socket

s= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

msg = b"Hello WORLD"
s.sendto(msg, ('localhost', 10000))
data , addr = s.recvfrom(16)
print(data)