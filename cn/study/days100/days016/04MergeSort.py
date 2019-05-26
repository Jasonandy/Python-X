"""
归并排序
"""
from time import time


def merge_sort(items, comp=lambda x, y: x <= y):
    """归并排序(分治法)"""
    if len(items) < 2:
        return items[:]
    mid = len(items) // 2
    left = merge_sort(items[:mid], comp)
    right = merge_sort(items[mid:], comp)
    return merge(left, right, comp)


def merge(items1, items2, comp):
    """合并(将两个有序的列表合并成一个有序的列表)"""
    items = []
    index, index2 = 0, 0
    while index < len(items1) and index2 < len(items2):
        if comp(items1[index], items2[index2]):
            items.append(items1[index])
            index += 1
        else:
            items.append(items2[index2])
            index2 += 1
    items += items1[index:]
    items += items2[index2:]
    return items


def main():
    origin = [1, 22, 13, 34, 55, 26, 12, 32, 32, 23, 45, 34, 78, 89, 67, 56, 12, 32, 92]
    print(origin)
    start_time = time()
    sort = merge_sort(origin)
    end_time = time()
    print('排序CostTime: %.2f (s) \n排序后的列表: %s ' % (end_time - start_time, sort))


if __name__ == '__main__':
    main()

