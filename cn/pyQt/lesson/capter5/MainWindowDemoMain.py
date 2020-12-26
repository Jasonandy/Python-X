import sys
from cn.pyQt.lesson.capter5 import MainWindowDemo

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget


class MainWindowDemoMain(QMainWindow):
    # 继承父类 相当于默认初始化构造函数
    class CenterForm(QMainWindow):
        def __init__(self, parent=None):
            super(MainWindowDemoMain, self).__init__(parent)
            # 设置主窗口的标题
            self.resize(800, 600)
            self.status = self.statusBar()
            self.status.showMessage('勿忘初心  方得始终', 6000)

        def center(self):
            # 获取屏幕坐标
            screen = QDesktopWidget().screenGeometry()
            print(screen.height())
            # 获取窗口坐标
            size = self.geometry()
            new_left = (screen.width() - size.width()) / 2
            new_top = (screen.height() - size.height()) / 2
            self.move(new_left, new_top)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('demo.ico'))
    mainWindows = QMainWindow()
    ui = MainWindowDemo.Ui_MainWindow()
    ui.setupUi(mainWindows)
    mainWindows.setWindowTitle("楚大点名器")
    mainWindows.show()
    sys.exit(app.exec_())