import socket
import os

def send_file(file_path, server_address):
    # 创建 UDP 套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    with open(file_path, 'rb') as file:
        file_data = file.read()

    file_name = os.path.basename(file_path)
    udp_socket.sendto(file_name.encode("utf-8"), server_address)
    udp_socket.sendto(file_data, server_address)

    # 关闭套接字
    udp_socket.close()

def send_directory(directory_path, server_address):
    # 获取目录下所有文件路径
    file_list = [os.path.join(directory_path, f) for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
    
    # 逐个发送文件
    for file in file_list:
        send_file(file, server_address)

def main():
    # 输入服务器的 IP 地址
    server_ip = input("请输入服务器的 IP 地址: ")
    server_port = 7788
    server_address = (server_ip, server_port)
    
    while True:
        # 输入要发送的文件或目录路径，输入 exit 退出
        file_path = input("请输入要发送的文件或目录路径（输入exit退出）: ")
        
        if file_path.lower() == "exit":
            break

        if os.path.isfile(file_path):
            # 如果是文件，发送单个文件
            send_file(file_path, server_address)
        elif os.path.isdir(file_path):
            # 如果是目录，递归发送目录下的所有文件
            send_directory(file_path, server_address)
        else:
            print("输入的不是有效的文件或目录路径，请重新输入。")

if __name__ == "__main__":
    main()
