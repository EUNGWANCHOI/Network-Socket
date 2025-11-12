from socket import *
import threading
import time

def send(sock):
    while True:
        msg = input(">>> ")
        sock.send(msg.encode('utf-8'))

def receive(sock):
    while True:
        recvData = sock.recv(1024)
        print("상대방 :", recvData.decode('utf-8'))

port = 8081


serverSock = socket(AF_INET, SOCK_STREAM) #소켓 객체 생성
serverSock.bind(('', port)) #포트 바인딩
serverSock.listen(1) #클라이언트의 접속을 기다림

print("%d번 포트에서 접속 대기중..." %port)

connectionSock, addr = serverSock.accept() #클라이언트 접속 허용

print(str(addr), "에서 접속하였습니다.")

sender = threading.Thread(target=send, args=(connectionSock,))
receiver = threading.Thread(target=receive, args=(connectionSock,))

sender.start()
receiver.start()

while True:
    time.sleep(1)
    pass