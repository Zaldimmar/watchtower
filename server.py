import socket
import threading
import os
import sys
import time
import datetime
import pyscreenshot as screenshot



sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT,1)
sock.bind(('localhost', 8080))
sock.listen(1)

while True:
    connection, client_address = sock.accept()

    img = screenshot.grab(childprocess=False)
    img.save('temp.png')
    data = 'temp.png'
    print('did it')
    with open(data, 'rb') as file:
        dts = file.read(1024)
        connection.send(dts)
        while dts != bytes(''.encode()):
            dts = file.read(1024)
            connection.send(dts)
        connection.close()
        print("connection closed")


