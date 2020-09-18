"""
文件读写缓冲
"""

# 行缓冲
# file = open("file.txt",'w',buffering=1)

# 指定缓冲大小
file = open("file.txt",'wb',buffering=10)

while True:
    info = input(">>")
    if not info:
        break
    file.write(info.encode())
    # file.flush() # 刷新缓冲

file.close()