import sys
from cn.pyQt.lesson.capter2 import MainWinBuddy

from PyQt5.QtWidgets import QApplication, QMainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindows = QMainWindow()
    ui = MainWinBuddy.Ui_MainWindow()
    ui.setupUi(mainWindows)
    mainWindows.setWindowTitle("学习绑定关系")
    mainWindows.show()
    sys.exit(app.exec_())


