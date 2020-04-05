import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication


class Example(QMainWindow):
    """
    演示
    """

    def __init__(self):
        super().__init__()
        self.initUI()

    # 初始化
    def initUI(self):
        btn1 = QPushButton("[Btn2]", self)
        btn1.move(30, 50)

        btn2 = QPushButton("[Btn1]", self)
        btn2.move(150, 50)

        # 按钮的点击事件绑定到 方法上面去
        btn1.clicked.connect(self.button_clicked)
        btn2.clicked.connect(self.button_clicked)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('事件 sender')
        self.show()

    def button_clicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    