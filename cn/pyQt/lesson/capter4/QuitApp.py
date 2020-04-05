import sys
from PyQt5.QtWidgets import QHBoxLayout, QWidget,QMainWindow, QPushButton, QApplication


class QuitApp(QMainWindow):
    def __init__(self):
        super(QuitApp,self).__init__()
        self.resize(300, 125)
        self.setWindowTitle('退出应用程序')

        # 添加btn
        self.button1 = QPushButton('退出')
        self.button1.clicked.connect(self.on_click_btn())

        layout = QHBoxLayout()
        layout.addWidget(self.button1)

        main_frame = QWidget()
        main_frame.setLayout(layout)
        self.setCentralWidget(main_frame)

    def on_click_btn(self):
        sender = self.sender()
        print(sender.text() + '按钮被按下')
        ap = QApplication.instance()
        # 退出应用程序
        ap.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QuitApp()
    main.show()
    sys.exit(app.exec_())

