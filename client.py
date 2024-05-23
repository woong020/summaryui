import socket
import os


def send_file(host='52.79.177.136', port=8080):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    file_path = r'C:/Users/ADMIN/Desktop/logo.png'  # 전송할 파일의 경로를 설정

    # 신호 전송: 파일 전송 신호 (1)
    client_socket.send(b'1')

    # 파일명과 확장자 분리
    file_name = os.path.basename(file_path)
    file_name_bytes = file_name.encode('utf-8')
    file_name_length = len(file_name_bytes)

    # 파일명 길이를 먼저 전송
    client_socket.send(file_name_length.to_bytes(4, 'big'))
    # 파일명 전송
    client_socket.send(file_name_bytes)

    with open(file_path, 'rb') as f:
        data = f.read(1024)
        while data:
            client_socket.sendall(data)
            data = f.read(1024)

    print("File sent successfully.")
    client_socket.close()


def send_delete_signal(host='52.79.177.136', port=8080):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # 신호 전송: 파일 삭제 신호 (2)
    client_socket.send(b'2')

    # 서버의 응답 메시지 수신
    response = client_socket.recv(1024).decode('utf-8')
    print(f"Server response: {response}")


def send_summary_signal(host='52.79.177.136', port=8080):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # 신호 전송: 요약 신호 (3)
    client_socket.send(b'3')

    # 서버의 응답 메시지 수신
    response = client_socket.recv(1024).decode('utf-8')
    return response