import sys
from cn.pyQt.lesson.capter1 import GridLayout

from PyQt5.QtWidgets import QApplication, QMainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindows = QMainWindow()
    ui = GridLayout.Ui_MainWindow()
    ui.setupUi(mainWindows)
    mainWindows.setWindowTitle("这是关于栅格布局的测试")
    mainWindows.show()
    sys.exit(app.exec_())


