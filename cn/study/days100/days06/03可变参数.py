"""
可变参数的学习
严格上来讲文件的名字是不能有中文的
但是这里为了学习的时候可以快速的找到资料
因此用中文表达了
"""


# 在参数名前面的*表示args是一个可变参数
# 即在调用add函数时可以传入0个或多个参数
def add(*args):
    total = 0
    for val in args:
        total += val
    return total


# 函数的参数是不定的
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
print(add(1, 3, 5, 7, 9))
