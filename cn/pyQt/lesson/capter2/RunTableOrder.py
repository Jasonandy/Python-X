import sys
from cn.pyQt.lesson.capter2 import TabOrder

from PyQt5.QtWidgets import QApplication, QMainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindows = QMainWindow()
    ui = TabOrder.Ui_MainWindow()
    ui.setupUi(mainWindows)
    mainWindows.setWindowTitle("Table Order ")
    mainWindows.show()
    sys.exit(app.exec_())


