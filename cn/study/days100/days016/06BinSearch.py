"""
折半查找
"""
from time import time


def bin_search(items, key):
    """折半查找"""
    start, end = 0, len(items) - 1
    while start <= end:
        mid = (start + end) // 2
        if key > items[mid]:
            start = mid + 1
        elif key < items[mid]:
            end = mid - 1
        else:
            return mid
    return -1


def main():
    origin = [1, 22, 13, 34, 55, 26, 12, 32, 32, 23, 45, 34, 78, 89, 67, 56, 12, 32, 92]
    print(origin)
    start_time = time()
    sort = bin_search(origin, 26)
    end_time = time()
    print('排序CostTime: %.2f (s) \n排序后的列表: %s ' % (end_time - start_time, sort))


if __name__ == '__main__':
    main()

