import socket
import sys
import threading
import time
import os
import datetime

class Client:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 8080))

    try:
        data = sock.recv(1024)
        sfname = str(datetime.datetime.now().date()).replace('-', "") + str(datetime.datetime.now().time()).split('.')[0].replace(':', "")
        file = open(sfname + '.png', 'wb')
        while data != bytes(''.encode()):
            file.write(data)
            data = sock.recv(1024)
        sock.sendall(b'File recieved')
        print("File accepted and written to " + sfname + ".png")

    except:
        print("You messed up")

    finally:
        print('closing socket')
        sock.close()

start = Client()