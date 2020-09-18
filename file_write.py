"""
文件写操作示例
"""

# 打开文件
# file = open("file.txt",'wb')

file = open("file.txt",'a') # 追加

# 写入内容
# n = file.write(b"hello,xxxxxx\n")
# print("写入字符:",n)
#
# file.write("哎呀，干啥\n".encode())

# 写入的内容
info = ["感恩白衣死战\n","龙魂不死\n"]
file.writelines(info)


file.close()