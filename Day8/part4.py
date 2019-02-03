# UDP Server code

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM )
s.bind(("", 10000))
s.settimeout(40)
while True:
    data, addr = s.recvfrom(16)
    resp = b"GET OFF My Lawn"
    s.sendto(resp,addr)
    print('From Client',data)
