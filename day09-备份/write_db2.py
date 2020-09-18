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
# 写入多个数据
data_list = [
    ("Davy",17,"m",81),
    ("sunny",19,"w",75),
    ("herry",16,"w",65),
    ("shelly",17,"m",95),
    ("serry",18,"m",66)
]
sql = "insert into cls (name,age,sex,score) values (%s,%s,%s,%s);"
try:
    cur.executemany(sql,data_list)
    db.commit()
except:
    db.rollback()
# 关闭
cur.close()
db.close()