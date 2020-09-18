from socket import *

# 服务器地址
ADDR = ("127.0.0.1",8888)

# 创建udp套接字
udp_socket = socket(AF_INET,SOCK_DGRAM)

# 发送后接收，与服务端配合
while True:
    word = input("Word:")
    if not word:
        break
    udp_socket.sendto(word.encode(),ADDR) # 发送单词

    data,addr = udp_socket.recvfrom(1024) # 接收单词解释
    print("%s: %s"%(word,data.decode()))

# 关闭套接字
udp_socket.close()