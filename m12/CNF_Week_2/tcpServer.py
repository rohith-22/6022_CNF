import socket
import random
import threading


port_list = []
def Main():
    host  = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.bind((host,port))
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.listen(10)

    while True:
        c, addr = s.accept()
        print ('connection from : '+ str(addr))
        port_list.append(addr[1])
        initial = 'welcome'
        c.send(str(initial).encode())
        threading.Thread(target = Guess, args = (c, addr)).start()

def puzzle(c, addr):
    count = 0
    connection = True

    while connection:
        
            

if __name__ == '__main__':
    Main()