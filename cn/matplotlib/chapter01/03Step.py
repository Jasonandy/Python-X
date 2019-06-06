"""
画图
"""
import numpy as np
import matplotlib.pyplot as plt


def function_picture(t):
    """
    函数
    :param t: e-t * cos(x pi t)
    :return:
    """
    return np.exp(-t) * np.cos(2 * np.pi * t)


def show_picture():
    """
    展示结果图片
    :return:
    """
    # 曲线要光滑,步长尽可能小
    x = np.arange(0, 5, 0.000001)
    # 该图在上半部分
    plt.subplot(2, 1, 1)
    plt.plot(x, function_picture(x))
    # 该图在下半部分
    plt.subplot(2, 1, 2)
    # ‘r--’:r表示红色，--表示控制曲线格式的字符
    plt.plot(x, np.cos(2 * np.pi * x), 'r--')
    plt.show()


def show_heart():
    """
    心形函数
    :return:
    """
    init = np.arange(-np.pi, np.pi, 0.001)
    y = np.subtract(np.multiply(2, np.cos(init)), np.cos(np.multiply(2, init)))
    x = np.subtract(np.multiply(2, np.sin(init)), np.sin(np.multiply(2, init)))
    plt.plot(x, y)
    plt.fill_between(x, y, facecolor='red')
    plt.show()


def run():
    show_picture()
    show_heart()


if __name__ == '__main__':
    run()
