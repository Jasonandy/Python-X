import sys
from cn.pyQt.lesson.capter3 import MainWinMenuToolBar

from PyQt5.QtWidgets import QApplication, QMainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindows = QMainWindow()
    ui = MainWinMenuToolBar.Ui_MainWindow()
    ui.setupUi(mainWindows)
    mainWindows.setWindowTitle("菜单和工具条")
    mainWindows.show()
    sys.exit(app.exec_())


