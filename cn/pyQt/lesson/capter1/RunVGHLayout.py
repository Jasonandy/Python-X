import sys
from cn.pyQt.lesson.capter1 import VGHLayout

from PyQt5.QtWidgets import QApplication, QMainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindows = QMainWindow()
    ui = VGHLayout.Ui_MainWindow()
    ui.setupUi(mainWindows)
    mainWindows.setWindowTitle("垂直水平栅格布局")
    mainWindows.show()
    sys.exit(app.exec_())


