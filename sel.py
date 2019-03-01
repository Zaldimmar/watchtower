import socket
import select

class selex():

    def __init__(self):
        self.s = socket.socket()
        self.s.connect(('localhost', 1235))

        while 1:
            #print("yeet")
            sel = select.select([self.s],[],[],0)
            if sel[0]:
                print(sel[0][0].recv(2048))



if __name__ == '__main__':
    selex()
