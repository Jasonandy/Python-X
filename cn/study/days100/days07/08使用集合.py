"""
Python中允许通过一些特殊的方法来为某种类型或数据结构自定义运算符（后面的章节中会讲到），
上面的代码中我们对集合进行运算的时候可以调用集合对象的方法，也可以直接使用对应的运算符，
例如&运算符跟intersection方法的作用就是一样的，但是使用运算符让代码更加直观。
"""


def main():
    set1 = {1, 2, 3, 3, 3, 2}
    # 数据会进行去重操作
    print(set1)
    # {1, 2, 3}
    print('Length =', len(set1))
    set2 = set(range(1, 10))
    print(set2)
    # {1, 2, 3, 4, 5, 6, 7, 8, 9}
    set1.add(4)
    set1.add(5)
    print(set1)
    # {1, 2, 3, 4, 5}
    set2.update([11, 12])
    print(set2)
    # {1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12}
    set2.discard(5)
    print(set2)
    # discard 放弃更改
    # {1, 2, 3, 4, 6, 7, 8, 9, 11, 12}
    # remove的元素如果不存在会引发KeyError
    if 4 in set2:
        set2.remove(4)
    print(set2)
    # 遍历集合容器
    for elem in set2:
        print(elem ** 3, end=' ')
    print()
    # 将元组转换成集合
    set3 = set((1, 2, 3, 3, 2, 1))
    print(set3.pop())
    # pop 头弹出去就没了
    print(set3)
    print("集合set1:", set1)
    print("集合set2:", set2)
    print("集合set3:", set3)
    # 集合的交集、并集、差集、对称差运算
    print("集合1 2 交集：", set1 & set2)
    # print(set1.intersection(set2))
    print("集合1 2 并集：", set1 | set2)
    # print(set1.union(set2))
    print("集合1 - 集合2：", set1 - set2)
    # print(set1.difference(set2))
    print("集合1 ^ 集合2(差集)", set1 ^ set2)
    # print(set1.symmetric_difference(set2))
    # 判断子集和超集
    print("判断子集和超集{包含关系}")
    print(set2 <= set1)
    # print(set2.issubset(set1))
    print(set3 <= set1)
    # print(set3.issubset(set1))
    print(set1 >= set2)
    # print(set1.issuperset(set2))
    print(set1 >= set3)
    # print(set1.issuperset(set3))


if __name__ == '__main__':
    main()

