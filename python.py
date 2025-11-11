from socket import *

serverSock = socket(AF_INET, SOCK_STREAM) #소켓 객체 생성
serverSock.bind(('', 8080)) #포트 바인딩
serverSock.listen(1) #클라이언트의 접속을 기다림

connestionSock, addr = serverSock.accept() #클라이언트 접속 허용