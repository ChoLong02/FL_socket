# -*- coding: utf-8 -*-
import socket
from _thread import *

# 접속한 클라이언트마다 새로운 thread 생성
def thread_socket(client_socket, addr):
    print(f'Connected by: {addr[0]}, {addr[1]}')
    
    # 클라이언트 연결 해제까지 반복
    while True:
        
        try:
            # 클라이언트 -> 데이터 수신 -> 클라이언트 다시 전송(에코)
            data = client_socket.recv(1024)
            
            if not data:
                print(f'Disconnected by: {addr[0]}, {addr[1]}')
                break
            
            print(f'Received from: {addr[0]}, {addr[1]}, {data.decode()}')
            
            for client in client_sockets:
                if client != client_socket:
                    client.send(data)
                    
        except ConnectionResetError as e:
            print(f'Disconnected by: {addr[0]}, {addr[1]}')
            break
        
    if client_socket in client_sockets:
        client_sockets.remove(client_socket)
        print(f'Remove Client List: {len(client_sockets)}')
    client_socket.close()
    

client_sockets = []  # 서버에 접속할 클라이언트 목록
HOST = '127.0.0.1'
PORT = 9999

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('', PORT))
server_socket.listen()

print('::::::::::::::::::')
print(':: SERVER START ::')
print('::::::::::::::::::')

try:
    while True:
        print(':: WAIT')
        
        client_socket, addr = server_socket.accept()
        client_sockets.append(client_socket)
        start_new_thread(thread_socket, (client_socket, addr))
        print(f'Client List: ', len(client_sockets))
except Exception as e:
    print(f'Error: {e}')        
finally:
    server_socket.close()