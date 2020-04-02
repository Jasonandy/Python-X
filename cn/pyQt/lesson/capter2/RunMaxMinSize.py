import sys
from cn.pyQt.lesson.capter2 import MaxMinSize

from PyQt5.QtWidgets import QApplication, QMainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindows = QMainWindow()
    ui = MaxMinSize.Ui_MainWindow()
    ui.setupUi(mainWindows)
    mainWindows.setWindowTitle("默认的最大最小尺寸学习")
    mainWindows.show()
    sys.exit(app.exec_())


