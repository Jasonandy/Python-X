from time import time


def bubble_sort(origin_items, comp=lambda x, y: x > y):
    """
    高质量冒泡排序(搅拌排序)
    :param origin_items:
    :param comp:
    :return:
    """
    items = origin_items[:]
    for i in range(len(items) - 1):
        swapped = False
        for j in range(i, len(items) - 1 - i):
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if swapped:
            swapped = False
            for j in range(len(items) - 2 - i, i, -1):
                if comp(items[j - 1], items[j]):
                    items[j], items[j - 1] = items[j - 1], items[j]
                    swapped = True
        if not swapped:
            break
    return items


def main():
    origin = [1, 22, 13, 34, 55, 26, 12, 32, 32, 23, 45, 34, 78, 89, 67, 56, 12, 32, 92]
    print(origin)
    start_time = time()
    sort = bubble_sort(origin)
    end_time = time()
    print('排序CostTime: %.2f (s) \n排序后的列表: %s ' % (end_time - start_time, sort))


if __name__ == '__main__':
    main()

