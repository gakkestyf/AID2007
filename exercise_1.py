"""
单词本特征 ： 1. 每个单次占一行
            2.  单次解释之间一定有空格
            3.  后面的单次一定比前面的单次大
要求 ： 编写一个函数，参数传入一个单次，返回
这个单次所在的那一行内容,如果这个单次没有则返回None
"""

def query_word(word):
    """
    :param word: 目标单词
    :return: 单词所在行
    """
    file = open('dict.txt') # 读方式打开
    # 逐行比对的方法
    for line in file:
        # 提取出这一行的单词
        tmp = line.split(' ')[0]
        # 如果遍历到的单词已经比目标单词大了，就没有必要再找了
        if tmp > word:
            file.close()
            return
        elif word == tmp:
            file.close()
            return line


result = query_word("abc")
print(result)