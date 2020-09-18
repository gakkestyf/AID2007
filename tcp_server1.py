"""
tcp 服务端基础实例

重点代码 ！！
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

    # 收发消息
    while True:
        # 链接的另外一端结束 此时 recv会返回空字节串
        data = connfd.recv(1024)
        # 收到##或者data为空字节串时 表示客户端结束
        if not data or data == b"##":
            break

        print("接收到：",data.decode())

        connfd.send(b"Thanks")

    connfd.close()

# 关闭套接字
tcp_socket.close()


