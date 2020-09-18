"""
pymysql 基本模型
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
# 数据操作


# 关闭
cur.close()
db.close()