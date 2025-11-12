from socket import *
import threading
import time

def send(sock):
    while True:
        sendData = input('>>>')
        sock.send(sendData.encode('utf-8'))

def receive(sock):
    while True:
        recvData = sock.recv(1024)
        print('상대방 :', recvData.decode('utf-8'))

port = 8081

clientSock = socket(AF_INET, SOCK_STREAM) #소켓 객체 생성
clientSock.connect(('localhost', 8081)) #서버에 접속

print('접속완료')

sender = threading.Thread(target=send, args=(clientSock,))
receiver = threading.Thread(target=receive, args=(clientSock,))

sender.start()
receiver.start()

while True:
    time.sleep(1)
    pass