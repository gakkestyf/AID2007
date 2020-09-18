"""
打开文件 示例
"""

# 打开文件

# 读方法 文件必须存储
# file = open("../day02/mul.py",'r')

# 写方法 文件不存在则创建
# file = open("file.txt",'w')

# 追加
file = open("file.txt",'a')

# 读写文件
print(file) # 文件对象

# 关闭文件
file.close()


