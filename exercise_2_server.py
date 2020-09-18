"""
从客户端上传一张图片到服务端，上传后
客户端结束，服务端继续运行。

要求： 图片可能比较大，不能一次读取

客户端 ： 一边读取一遍发送
服务端 ： 一边接收一边写入
"""
from socket import *

# 创建tcp套接字
tcp_socket = socket(AF_INET,SOCK_STREAM)

# 绑定地址
tcp_socket.bind(('0.0.0.0',8888))

# 设置监听
tcp_socket.listen(5)

while True:
    # 处理客户端链接 (阻塞函数)
    print("Waiting for connect...")
    connfd,addr = tcp_socket.accept()
    print("Connect from",addr)

    # 接收图片
    file = open("test.jpg",'wb')
    while True:
        data = connfd.recv(1024) # 接收内容
        if not data:
            break
        file.write(data) # 写入本地

    file.close()
    connfd.close()

# 关闭套接字
tcp_socket.close()






