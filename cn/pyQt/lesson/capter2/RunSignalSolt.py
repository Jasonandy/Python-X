import sys
from cn.pyQt.lesson.capter2 import MainWinSignalSlot

from PyQt5.QtWidgets import QApplication, QMainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindows = QMainWindow()
    ui = MainWinSignalSlot.Ui_MainWindow()
    ui.setupUi(mainWindows)
    mainWindows.setWindowTitle("信号与槽的学习")
    mainWindows.show()
    sys.exit(app.exec_())


