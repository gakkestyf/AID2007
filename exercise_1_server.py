"""
使用udp套接字完成
编写客户端和服务端，客户端可以循环的输入单词，
从服务端那里获取单词的解释，打印出来

服务端，接收客户端的单词，然后通过数据库查询得到
单次解释发送给客户端，让客户端去打印

提示： dict --》 words
"""

from socket import *
import pymysql

# 服务器地址
ADDR = ('0.0.0.0', 8888)


class Database:
    def __init__(self):
        self.db = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='123456',
            database='dict',
            charset='utf8')
        self.cur = self.db.cursor()

    def close(self):
        # 关闭
        self.cur.close()
        self.db.close()

    # 查询单词
    def find_word(self, word):
        sql = "select mean from words where word=%s;"
        self.cur.execute(sql, [word])
        result = self.cur.fetchone()  # (mean,)
        if result:
            return result[0]
        else:
            return "Not Found"


def main():
    # 创建udp套接字
    udp_socket = socket(AF_INET, SOCK_DGRAM)
    # 绑定地址
    udp_socket.bind(ADDR)

    db = Database()  # 数据库处理对象

    # 接收消息
    while True:
        # 接收单词
        data, addr = udp_socket.recvfrom(1024)
        # 查单词
        mean = db.find_word(data.decode())
        # 发送单词解释
        udp_socket.sendto(mean.encode(), addr)

    # 关闭套接字
    db.close()
    udp_socket.close()


if __name__ == '__main__':
    main()
