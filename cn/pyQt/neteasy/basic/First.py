import sys

from PyQt5.QtWidgets import QApplication, QWidget


if __name__ == '__main__':
    """
     这里是主函数  判断是不是当前执行函数
    __main__
    """
    print(__name__)
    # 创建QApplication类的实例
    app = QApplication(sys.argv)
    # ['E:/PyCharmSpace/Python-X/cn/pyQt/neteasy/basic/First.py'] 参数
    print(sys.argv)
    # 创建一个窗口
    w = QWidget()
    # 设置窗口的尺寸
    w.resize(400, 200)
    # 移动窗口  坐标原点在左上角
    w.move(300, 300)

    # 设置窗口的标题
    w.setWindowTitle('第一个基于PyQt5的桌面应用')
    # 显示窗口
    w.show()

    # 进入程序的主循环、并通过exit函数确保主循环安全结束
    sys.exit(app.exec_())
