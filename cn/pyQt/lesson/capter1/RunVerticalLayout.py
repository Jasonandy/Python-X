import sys
from cn.pyQt.lesson.capter1 import VerticalLayout

from PyQt5.QtWidgets import QApplication, QMainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindows = QMainWindow()
    ui = VerticalLayout.Ui_MainWindow()
    ui.setupUi(mainWindows)
    mainWindows.setWindowTitle("这是关于垂直布局的测试")
    mainWindows.show()
    sys.exit(app.exec_())


