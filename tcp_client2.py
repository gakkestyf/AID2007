"""
tcp客户端示例2
多个客户端循环发送消息
"""
from socket import *

while True:

    msg = input(">>")
    if not msg:
        break

    tcp_socket = socket()
    tcp_socket.connect(('127.0.0.1',8888))
    tcp_socket.send(msg.encode())
    data = tcp_socket.recv(1024)
    print("from Server：",data.decode())
    tcp_socket.close()