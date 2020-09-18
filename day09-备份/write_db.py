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
# 写数据库操作
try:
    sql = "update cls set score=100 where id=1;"
    cur.execute(sql)
    db.commit()  # 提交写操作
except:  # 如果报错
    db.rollback()  # 回滚，之前语句全部失效
# 关闭
cur.close()
db.close()
