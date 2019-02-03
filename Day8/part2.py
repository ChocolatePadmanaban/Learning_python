# Creating a server

import  socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("",9002))
s.listen(5)
s.settimeout(10)
while True:
    c, a = s.accept()
    print("Received  connection from",a)
    temp = "Hello "+ str(a[0])
    c.send(bytes(temp,'utf-8'))
    c.close()

