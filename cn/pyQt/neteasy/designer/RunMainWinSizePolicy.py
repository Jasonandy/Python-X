import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

from pyQt.neteasy.designer import MainWinSizePolicy

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = MainWinSizePolicy.Ui_MainWindow()
    # 向主窗口上添加控件
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())