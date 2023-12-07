import socket
import os

def receive_file(udp_socket):
    # 接收文件名和发送方地址
    file_name_data, sender_addr = udp_socket.recvfrom(1024)
    file_name = file_name_data.decode("utf-8")

    # 接收文件数据
    file_data, _ = udp_socket.recvfrom(1024 * 1024)  # 假设文件大小 < 1MB

    # 写入文件
    with open(file_name, 'wb') as file:
        file.write(file_data)

    print(f"从 {sender_addr} 收到文件 '{file_name}'.")

def main():
    # 创建 UDP 套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    host = socket.gethostbyname(socket.gethostname())
    local_addr = (host, 7788)
    udp_socket.bind(local_addr)

    while True:
        # 接收文件
        receive_file(udp_socket)

if __name__ == "__main__":
    main()
