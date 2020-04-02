import sys
from cn.pyQt.lesson.capter1 import SpacersLayout

from PyQt5.QtWidgets import QApplication, QMainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindows = QMainWindow()
    ui = SpacersLayout.Ui_MainWindow()
    ui.setupUi(mainWindows)
    mainWindows.setWindowTitle("表单布局学习")
    mainWindows.show()
    sys.exit(app.exec_())


