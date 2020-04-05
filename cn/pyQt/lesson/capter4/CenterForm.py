import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget


# 继承父类 相当于默认初始化构造函数
class CenterForm(QMainWindow):
    def __init__(self, parent=None):
        super(CenterForm, self).__init__(parent)

        # 设置主窗口的标题
        self.setWindowTitle('主窗口居中')
        self.resize(600, 600)

    def center(self):
        # 获取屏幕坐标
        screen = QDesktopWidget().screenGeometry()
        # 获取窗口坐标
        size = self.geometry()
        new_left = (screen.width() - size.width())/2
        new_top = (screen.height()-size.height())/2
        self.move(new_left,new_top)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = CenterForm()
    main.show()
    sys.exit(app.exec_())

