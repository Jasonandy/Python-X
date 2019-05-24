"""
字典是另一种可变容器模型，类似于我们生活中使用的字典，
它可以存储任意类型对象，与列表、集合不同的是，字典的每个元素都是由一个键和一个值组成的“键值对”，键和值通过冒号分开。
下面的代码演示了如何定义和使用字典。
"""


def main():
    print("--->字典的学习---->")
    scores = {'骆昊': 95, '白元芳': 78, '狄仁杰': 82}
    # 通过键可以获取字典中对应的值
    print(scores['骆昊'])
    print(scores['狄仁杰'])
    # 对字典进行遍历(遍历的其实是键再通过键取对应的值)
    for elem in scores:
        print('%s\t--->\t%d' % (elem, scores[elem]))
    # 更新字典中的元素
    scores['白元芳'] = 65
    scores['诸葛王朗'] = 71
    # 添加元素
    scores.update(冷面=67, 方启鹤=85)
    print(scores)
    # 打印 如果存在则打印
    if '武则天' in scores:
        print(scores['武则天'])
    print(scores.get('武则天'))
    # print none
    # get方法也是通过键获取对应的值但是可以设置默认值
    print(scores.get('武则天', 8))
    # 删除字典中的元素
    print(scores.popitem())
    print(scores.popitem())
    # 有的话直接出来 没有的话用默认的值
    print(scores.get('骆昊', 89))
    #
    print(scores.pop('骆昊', 100))
    # 清空字典
    scores.clear()
    print(scores)


if __name__ == '__main__':
    main()

