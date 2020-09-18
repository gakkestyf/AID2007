"""
tcp 服务端基础实例
"""

from socket import *

# 创建tcp套接字
tcp_socket = socket(AF_INET,SOCK_STREAM)

# 绑定地址
tcp_socket.bind(('0.0.0.0',8888))

# 设置监听
tcp_socket.listen(5)

# 处理客户端链接 (阻塞函数)
print("Waiting for connect...")
connfd,addr = tcp_socket.accept()
print("Connect from",addr)

# 收发消息
data = connfd.recv(1024)
print("接收到：",data.decode())

connfd.send(b"Thanks")

# 关闭套接字
connfd.close()
tcp_socket.close()


