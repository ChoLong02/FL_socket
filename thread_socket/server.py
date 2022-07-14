# -*- coding: utf-8 -*-
import socket
from _thread import *

# 접속한 클라이언트마다 새로운 thread 생성
def thread_socket(client_socket, addr):
    print(f'Connected by: {addr[0]}, :, {addr[1]}')
    
    # 클라이언트 연결 해제까지 반복
    while True:
        
        try:
            data = client_socket.recv(1024)
            
            if not data:
                print(f'Disconnected by: {addr[0]}, :, {addr[1]}')
                break
            
            print(f'Received from: {addr[0]}, :, {addr[1]}, {data.decode()}')
            
            client_socket.send(data)
        except ConnectionResetError as e:
            print(f'Disconnected by: {addr[0]}, :, {addr[1]}')
            break
        
    client_socket.close()
    

HOST = '127.0.0.1'
PORT = 9999

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen()

print('::::::::::::::::::')
print(':: SERVER START ::')
print('::::::::::::::::::')

while True:
    print('::     WAIT     ::')
    print('::::::::::::::::::')
    
    client_socket, addr = server_socket.accept()
    start_new_thread(thread_socket, (client_socket, addr))

server_socket.close()