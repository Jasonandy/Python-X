"""
画图看看
"""
import matplotlib.pyplot as plt


def show_ze_xian():
    """
    绘出折线
    :return:
    """
    plt.plot([1, 2, 3, 6, 8], [5, 7, 4, 8, 9])
    plt.show()


def show_test():
    """
    双折线
    :return:
    """
    x = [1, 2, 3]
    y = [5, 7, 4]
    x2 = [1, 2, 3]
    y2 = [10, 14, 12]
    plt.plot(x, y, label='First Line')
    plt.plot(x2, y2, label='Second Line')
    plt.show()


def run():
    show_ze_xian()
    show_test()


if __name__ == '__main__':
    run()
