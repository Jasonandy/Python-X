"""
map
"""


def square(x):
    return x ** 2


#  返回的是迭代器对象
map_a = map(square, [1, 2, 3, 4, 5])
map_b = map(lambda x: x ** 2, [1, 2, 3, 4, 5])
map_c = map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])

print(map_a)
print(list(map_a))

print(map_b)
print(list(map_b))

print(map_c)
print(list(map_c))

