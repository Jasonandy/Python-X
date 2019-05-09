from random import randint

"""
 函数的参数 by Jason
"""


# 有一个默认值 n = 2
def roll_dice(n=2):

    """
    摇色子
    :param n: 色子的个数
    :return: n颗色子点数之和
    """
    total = 0
    for _ in range(n):
        # randint 随机的int数据 1-6
        total += randint(1, 6)
    return total


# 数据相加 参数可变 且顺序也是可以调整的 要和java做好区分
def add(a=0, b=0, c=0):
    return a + b + c


# 如果没有指定参数那么使用默认值摇两颗色子
print(roll_dice())
# 摇三颗色子
print(roll_dice(6))
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
# 传递参数时可以不按照设定的顺序进行传递
print(add(c=50, a=100, b=200))
