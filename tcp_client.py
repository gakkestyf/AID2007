"""
tcp客户端基础实例
"""

from socket import *

# 创建tcp套接字 默认就是tcp套接字
tcp_socket = socket()

# 发起链接
tcp_socket.connect(('127.0.0.1',8888))

# 收发消息
msg = input(">>")
tcp_socket.send(msg.encode())

data = tcp_socket.recv(1024)
print("From server:",data.decode())

# 关闭套接字
tcp_socket.close()

