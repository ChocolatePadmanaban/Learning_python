# Server code for real

import socket
import sys
import pickle

class SimpleObject(object):

    def __init__(self, name):
        self.name = name

def Receive_Pickle():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 10001    )
    print('starting up on {} port {}'.format(*server_address))
    sock.bind(server_address)
    sock.listen(1)
    while True:
        print('waiting for a connection')
        connection, client_address = sock.accept()

        try:
            print('connection from', client_address)

            # Receive the data in small chunks and retransmit it
            while True:
                data = connection.recv(10000)
                if data:
                    data = pickle.loads(data)
                    print('received {!r}'.format(data.name))
                    print('sending data back to the client')
                    connection.sendall(data.name.upper().encode('utf-8'))
                else:
                    print('no data from', client_address)
                    break
        finally:
            # Clean up the connection
            connection.close()

if __name__ == "__main__":
    Receive_Pickle()