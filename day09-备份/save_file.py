"""
存储二进制文件
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
with open("66", "rb") as f:
    date = f.read()
try:
    sql = "update cls set image=%s where id=1"
    cur.execute(sql,[date])
    db.commit()
except:
    db.rollback()

# 关闭
cur.close()
db.close()
