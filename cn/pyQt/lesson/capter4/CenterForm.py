import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget
from PyQt5.QtGui import QIcon


# 继承父类 相当于默认初始化构造函数
class CenterForm(QMainWindow):
    def __init__(self, parent=None):
        super(CenterForm, self).__init__(parent)
        # 设置主窗口的标题
        self.setWindowTitle('设置主体窗口')
        self.resize(800, 600)
        self.status = self.statusBar()
        self.status.showMessage('勿忘初心  方得始终', 6000)

    def center(self):
        # 获取屏幕坐标
        screen = QDesktopWidget().screenGeometry()
        print(screen.height())
        # 获取窗口坐标
        size = self.geometry()
        new_left = (screen.width() - size.width())/2
        new_top = (screen.height()-size.height())/2
        self.move(new_left, new_top)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('cn/pyQt/lesson/capter4/lol.ico'))
    main = CenterForm()
    main.show()
    sys.exit(app.exec_())

