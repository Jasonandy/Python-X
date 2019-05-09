"""
判断一个数是不是素数
"""
print("== muns 是否为素数 ===")
nums = int(input(" nums = "))


# 判断一个数是不是素数
def is_prime(num):
    for factor in range(2, num):
        if num % factor == 0:
            return False
    # return True if num != 1 else False
    return True if num != 1 else False


print(is_prime(nums))


