import socket

def server():
    # 服务器端
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 获取本地主机名
    host = socket.gethostname()
    port = 7788
    server_address = (host, port)

    # 绑定地址和端口
    server_socket.bind(server_address)

    # 监听连接
    server_socket.listen(1)
    print(f'等待连接，服务器地址：{host}:{port}')

    # 接受连接
    client_socket, client_address = server_socket.accept()
    print('建立连接：', client_address)

    while True:
        # 接收客户端发送的数据
        data = client_socket.recv(1024)
        if not data:
            break
        print('收到的数据：', data.decode('utf-8'))

    # 关闭连接
    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    server()
