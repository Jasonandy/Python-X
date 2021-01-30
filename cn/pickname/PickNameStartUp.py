import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from pickname import PickNameUi


class MainWindow(QMainWindow):

    def __init__(self):
        super(PickNameUi, self).__init__()
        self.setupUi()
        # 设置主窗口的标题
        self.status = self.statusBar()
        self.status.showMessage('勿忘初心  方得始终', 6000)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindows = MainWindow()
    ui = PickNameUi.Ui_MainWindow()
    ui.setupUi(mainWindows)
    mainWindows.setWindowTitle("楚大点名器")
    mainWindows.show()
    sys.exit(app.exec_())