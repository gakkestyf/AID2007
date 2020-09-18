"""
with 打开文件
"""

with open("file.txt",'r') as file:
    # with语句块，在这里可以使用file
    data = file.read()
    print(data)

# with语句块结束  file 自动销魂