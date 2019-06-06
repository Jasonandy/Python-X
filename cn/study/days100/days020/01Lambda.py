"""
lambda + filter

"""
import math


def lambda_a(a, b, c):
    return lambda x, y: a*x+(b**y)+c


fxa = lambda_a(1, 2, 3)


def is_sqr(x):
    return math.sqrt(x) % 1 == 0


new_list = filter(is_sqr, range(1, 101))
print(list(new_list))


def main():
    print(fxa(1, 2))


if __name__ == '__main__':
    main()

