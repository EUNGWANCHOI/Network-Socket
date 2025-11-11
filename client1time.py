from socket import *

clientSock = socket(AF_INET, SOCK_STREAM) #소켓 객체 생성
clientSock.connect(('127.0.0.1', 8080)) #서버에 접속

print("서버에 접속하였습니다.")
clientSock.send("나는 클라이언트야".encode('utf-8'))

print("메시지를 보냈습니다.")

data = clientSock.recv(1024)
print("받은 데이터 :", data.decode('utf-8'))