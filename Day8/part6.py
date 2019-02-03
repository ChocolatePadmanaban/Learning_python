# Server code in TCP/IP
# not completed

import socket
import sys

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('localhost', 10001)
print('starting up on 192.168.43.83, {} port {}'.format(*server_address))
sock.bind(("",10000))
sock.settimeout(40)
# Listen for incoming connections


while True:
    # Wait for a connection
    print('waiting for a connection')
    
    try:
        data, addr = sock.recvfrom(16)

        # Receive the data in small chunks and retransmit it
        while True:
            
            print('received {!r}'.format(data))
            if data:
                print('sending data back to the client')
                sock.send(data.upper(), addr)
            else:
                print('no data from', addr)
                break

    finally:
        sock.close()
        pass
        # Clean up the connection


# from another terminal connect $telnet localhost portno
