"""
学习测试
    [1 2 3]
    [[1 2]
     [3 4]]
    [[1 2]
     [3 4]
     [5 6]]
    [[1 2 3 4 5]]
    [1.+0.j 2.+0.j 3.+0.j]
    支持高级大量的维度数组与矩阵运算，此外也针对数组运算提供大量的数学函数库
"""
import numpy as np


def test_first():
    """
    测试
    :return:
    """
    a = np.array([1, 2, 3])
    print(a)


def test_2_wei():
    """
    二维
    :return:
    """
    a = np.array([[1, 2], [3, 4]])
    print(a)


def test_3_wei():
    """
    三维
    :return:
    """
    a = np.array([[1, 2], [3, 4], [5, 6]])
    print(a)


def min_dimension():
    """
    最小维数
    :return:
    """
    a = np.array([1, 2, 3, 4, 5], ndmin=2)
    print(a)


def complex_data():
    """
    复数
    :return:
    """
    a = np.array([1,  2,  3], dtype=complex)
    print(a)


def main():
    test_first()
    test_2_wei()
    test_3_wei()
    min_dimension()
    complex_data()


if __name__ == '__main__':
    main()

