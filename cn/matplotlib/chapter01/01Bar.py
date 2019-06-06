"""
条形直方图
"""
import matplotlib.pyplot as plt


def show_bar():
    """
    展示条形图
    :return:
    """
    x1 = [1, 3, 5, 7, 9]
    y1 = [5, 2, 7, 8, 2]
    plt.bar(x1, y1, label="Jason")

    x2 = [2, 4, 6, 8, 10]
    y2 = [8, 6, 2, 5, 6]
    plt.bar(x2, y2, label="Andy", color='g')
    plt.legend()
    plt.xlabel('Month')
    plt.ylabel('Weight')
    plt.title('JasonInternational \n jasonandy@hotmail.com')
    plt.show()


def run():
    show_bar()


if __name__ == '__main__':
    run()
