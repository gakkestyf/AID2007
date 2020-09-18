"""
文件读取示例
"""

# 打开文件 默认 r
file = open("file.txt",'r')

# 读取内容
# data = file.read()
# print(data)

# 大文件分批读取，data每次读取1024个字符
# while True:
#     data = file.read(1024)
#     # 读取到文件结尾继续读取会得到空字符串
#     if not data:
#         break
#     print(data,end="")

# 读取一行内容
# data = file.readline(8)
# print(data)
# data = file.readline()
# print(data)

# 读取所有行  如果有参数，则读取到参数字符个数所到行
# data = file.readlines(13)
# print(data)

# for迭代，每次获取一行
for line in file:
    print(line)

file.close()

