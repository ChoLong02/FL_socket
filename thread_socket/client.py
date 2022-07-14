# -*- coding: utf-8 -*-
import socket
from _thread import *

HOST = '127.0.0.1'
PORT = 9999

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))


def recv_data(client_socket):
    while True:
        data = client_socket.recv(1024)
        
        print(f'Receive: {repr(data.decode())}')
        print('')
        
        
start_new_thread(recv_data, (client_socket,))


while True:
    message = input('')
    if message == 'quit':
        break
    
    client_socket.send(message.encode())
    
    
client_socket.close()