"""
文件偏移量
"""

file = open("file.txt","wb+")

file.write(b"Hello world")
file.flush()

# 文件偏移位置
print(file.tell())

file.seek(5,0) # 以开头算，向后移动5个

data = file.read()
print(data)

file.close()