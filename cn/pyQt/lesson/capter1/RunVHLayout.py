import sys
from cn.pyQt.lesson.capter1 import VHLayout

from PyQt5.QtWidgets import QApplication, QMainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindows = QMainWindow()
    ui = VHLayout.Ui_MainWindow()
    ui.setupUi(mainWindows)
    mainWindows.setWindowTitle("垂直和水平布局")
    mainWindows.show()
    sys.exit(app.exec_())


