# import pymysql
# import re
#
# qp = pymysql.connect(
#     host="localhost",
#     port=3306,
#     user="root",
#     password="123456",
#     database="dict",
#     charset="utf8")
# date=[]
# cur = qp.cursor()
# x = open("/home/tarena/month02/day03/dict.txt")
# for i in x:
#     z = re.findall('\w+\S+\w+',i)
#
#     # sql = f"insert into cls name values {z[0]}"
#     print(z[0])
#     # try:
#     #     sql = "insert into words values()"
#     #     cur.execute(sql)
#     # qp.commit()  # 提交写操作
#     # except:  # 如果报错
#     #     qp.rollback()
#     # print(i)
# cur.close()
# qp.close()

import pymysql
import re

# 链接数据库 (如果连接本机数据库可以不写host，port)
db = pymysql.connect(
    user = 'root',
    password = '123456',
    database = 'dict',
    charset = 'utf8')

# 创建游标 (游标就是执行sql语句操作数据得到结果的对象)
cur = db.cursor()

data = [] # 存放匹配出的单词

# 数据操作
file = open("/home/tarena/month02/day03/dict.txt")

# 每次取一行 一个单词
for line in file:
    one_word = re.findall(r"(\w+)\s+(.*)",line)
    data.append(one_word[0])

# 插入数据库
try:
    sql = "insert into words (word,mean) values (%s,%s);"
    cur.executemany(sql,data)
    db.commit()
except Exception as e:
    print(e)
    db.rollback()
print(data)

# 关闭
cur.close()
db.close()