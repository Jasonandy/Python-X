import sys
from cn.pyQt.lesson.capter1 import HorizontalLayout

from PyQt5.QtWidgets import QApplication, QMainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindows = QMainWindow()
    ui = HorizontalLayout.Ui_MainWindow()
    ui.setupUi(mainWindows)
    mainWindows.setWindowTitle("这是关于布局的测试")
    mainWindows.show()
    sys.exit(app.exec_())


