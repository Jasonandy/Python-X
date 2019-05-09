"""
函数的定义和使用 - 计算组合数C(7,3)
Version: 0.1
Author: Jason
Date: 2019-05-09
"""

m = int(input("m = "))
n = int(input("n = "))


# 将求阶乘的功能封装成一个函数
# 注释和下面要空格两行 # 还要空格一个
def factorial(n):
    result = 1
    for num in range(1, n + 1):
        result *= num
    return result


# 注释写完后还要最后要空一行
print(factorial(m) // factorial(n) // factorial(m-n))
