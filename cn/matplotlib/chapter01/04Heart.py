"""
画心
"""
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import matplotlib.dates as dt
from mpl_toolkits.mplot3d import Axes3D

def show_heart():
    # 图形大小
    mpl.rcParams['font.size'] = '10'
    # 字体
    mpl.rcParams['font.weight'] = 'bold'
    fig = plt.figure()
    # 建立一个图形实例
    fig.add_subplot(111, facecolor='yellow', projection='3d')
    t = np.linspace(0, 2 * np.pi, 100)
    x = 16 * np.sin(t) ** 3
    y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)
    plt.plot(x, y, 'm-', linewidth=2)
    plt.grid(True)
    plt.show()


def run():
    show_heart()


if __name__ == '__main__':
    run()