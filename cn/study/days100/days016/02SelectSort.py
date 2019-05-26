"""
选择排序
"""
from time import time


# 选择排序
def select_sort(origin_items, comp=lambda x, y: x < y):
    """
    简单选择排序
    :param origin_items: 需要排序的数据 []
    :param comp:
    :return:
    """
    items = origin_items[:]
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    return items


def main():
    origin = [1, 22, 13, 34, 55, 26, 12, 32, 32, 23, 45, 34, 78, 89, 67, 56, 12, 32, 92]
    print(origin)
    start_time = time()
    sort = select_sort(origin)
    end_time = time()
    print('排序CostTime: %.2f (s) \n排序后的列表: %s ' % (end_time-start_time, sort))


if __name__ == '__main__':
    main()

