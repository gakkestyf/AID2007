from socket import *

# 创建tcp套接字 默认就是tcp套接字
tcp_socket = socket()

# 发起链接
tcp_socket.connect(('127.0.0.1',8888))

# 发送文件
filename = input(">>")
file = open(filename,'rb')
while True:
    data = file.read(1024) # 读取文件内容
    if not data:
        break
    tcp_socket.send(data) # 发送给服务端

# 关闭套接字
file.close()
tcp_socket.close()
