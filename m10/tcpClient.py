import socket
import threading
s=socket.socket()
port=5101
username=input("Enter user name:")
ip="127.0.0.1"
s.connect((ip,port))
def receiveMsg(sock):
    while True:
        msg=sock.recv(1024).decode()
        print(msg)
threading.Thread(target=receiveMsg,args=(s,)).start()
while True:
    tempMsg=input()
    msg=username+'>>'+tempMsg
    s.send(msg.encode())