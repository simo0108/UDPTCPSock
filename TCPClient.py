import socket

def client():
    # 客户端
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 手动输入服务器IP地址
    server_ip = input("输入IP: ")
    server_port = 7788
    server_address = (server_ip, server_port)

    # 连接服务器
    client_socket.connect(server_address)
    print(f'已连接：{server_ip}:{server_port}')

    while True:
        # 发送数据到服务器
        data_to_send = input('输入要发送给的消息(输入exit退出)：')
        client_socket.send(data_to_send.encode('utf-8'))
        if data_to_send=='exit':
            break

    # 关闭连接
    client_socket.close()

if __name__ == "__main__":
    client()
