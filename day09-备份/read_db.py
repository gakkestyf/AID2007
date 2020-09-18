"""
读数据库操作
"""
import pymysql

db = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="123456",
    database="stu",
    charset="utf8")
# 创建游标（执行sql语句操作数据得到结果）
cur = db.cursor()
# 查询数据操作
sql = "select * from cls;"
cur.execute(sql)


for i in cur:
    print(i)
# 获取一个结果
one = cur.fetchone()
print(one)
# 获取多个查询结果
many = cur.fetchmany(1)
print(many)

# 所有结果
all = cur.fetchall()
print(all)

# 关闭
cur.close()
db.close()
