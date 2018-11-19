import socket
import sys
import pickle

class SimpleObject(object):

    def __init__(self, name):
        self.name = name

def client(name = "Pradeeeeeeeeeep"):
    server_address = ('localhost', 10001)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(server_address)
    try:
        a = SimpleObject(name)
        message=pickle.dumps(a)
        sock.sendall(message)
        condition = True
        while condition:
            data = sock.recv(10000)
            if data:
                print('received {!r}'.format(data.decode('utf-8')))
                condition = False
            
    finally:
        print('closing socket')
        sock.close()
        return data.decode('utf-8')

if __name__ == '__main__':
    print(client())