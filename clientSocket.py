from socket import *
import threading
import time

clientSock = socket(AF_INET, SOCK_STREAM) #소켓 객체 생성
clientSock.connect(('localhost', 8080)) #서버에 접속