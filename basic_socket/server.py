# -*- coding: utf-8 -*-
import socket


HOST = '127.0.0.1'  # 접속할 서버 주소
PORT = 9999         # 클라이언트 접속 대기 포트번호

# 소켓 객체 생성(IPv4, TCP)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPv4, TCP

# 포트 사용중일 때 연결X 에러 해결
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# HOST(hostname or ip or ''), ''인경우 모든 네트워크 인터페이스로부터 접속 허용
# PORT(1~65535)
server_socket.bind((HOST, PORT))  # Tuple 타입으로 여러개 설정 가능

# 서버가 클라이언트 접속 허용
server_socket.listen()


# accept()에서 대기하다가 클라이언트 접속하면 새로운 소켓 리턴
client_socket, addr = server_socket.accept()

# 접속한 클라이언트의 주소
print(f'Connected by client: {addr}')

while True:
    # 클라이언트가 보낸 메시지 수신을 위해 대기
    data = client_socket.recv(1024)
    
    # 빈 문자열 수신시 종료
    if not data:
        break
    
    # 수신받은 문자열 출력
    print(f'Received from client: {addr}, {data.decode()}')
    
    # 받은 문자열 다시 클라이언트 전송(에코)
    client_socket.sendall(data)
    
# 소켓 종료
client_socket.close()
server_socket.close()