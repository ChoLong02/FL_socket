# -*- coding: utf-8 -*-
import socket


HOST = '127.0.0.1'  # ������ ���� �ּ�
PORT = 9999         # Ŭ���̾�Ʈ ���� ��� ��Ʈ��ȣ

# ���� ��ü ����(IPv4, TCP)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPv4, TCP

# ��Ʈ ������� �� ����X ���� �ذ�
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# HOST(hostname or ip or ''), ''�ΰ�� ��� ��Ʈ��ũ �������̽��κ��� ���� ���
# PORT(1~65535)
server_socket.bind((HOST, PORT))  # Tuple Ÿ������ ������ ���� ����

# ������ Ŭ���̾�Ʈ ���� ���
server_socket.listen()


# accept()���� ����ϴٰ� Ŭ���̾�Ʈ �����ϸ� ���ο� ���� ����
client_socket, addr = server_socket.accept()

# ������ Ŭ���̾�Ʈ�� �ּ�
print(f'Connected by client: {addr}')

while True:
    # Ŭ���̾�Ʈ�� ���� �޽��� ������ ���� ���
    data = client_socket.recv(1024)
    
    # �� ���ڿ� ���Ž� ����
    if not data:
        break
    
    # ���Ź��� ���ڿ� ���
    print(f'Received from client: {addr}, {data.decode()}')
    
    # ���� ���ڿ� �ٽ� Ŭ���̾�Ʈ ����(����)
    client_socket.sendall(data)
    
# ���� ����
client_socket.close()
server_socket.close()