import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider,
                             QVBoxLayout, QApplication)


class Example(QWidget):
    """
    继承父类QWidget
    http://code.py40.com/2004.html
    """
    # 初始化
    def __init__(self):
        super().__init__()
        self.initUI()

    # 设置初始化函数
    def initUI(self):

        # LCD 显示
        lcd = QLCDNumber(self)

        # 滑动的进度条
        sld = QSlider(Qt.Horizontal, self)

        # 垂直布局
        vbox = QVBoxLayout()

        # 添加两个Widget组件
        vbox.addWidget(lcd)
        vbox.addWidget(sld)
        # 设置布局
        self.setLayout(vbox)

        # 绑定信号和槽 (事件绑定到方法上去)
        sld.valueChanged.connect(lcd.display)

        # 设置相对坐标
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Signal[信号]&Slot[槽]')
        self.show()

    # 重写了 快捷键方法
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            print('Esc Closing ...')
            self.close()


if __name__ == '__main__':
    # 创建QApplication
    app = QApplication(sys.argv)
    # 实例化对象
    ex = Example()
    sys.exit(app.exec_())