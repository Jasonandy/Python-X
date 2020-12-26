'''
QLabel与伙伴控件
mainLayout.addWidget(控件对象,rowIndex,columnIndex,row,column)
'''

from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit, QLabel, QPushButton, QGridLayout
from PyQt5.QtGui import QIcon
import sys


# QDialog 一个对话框
class QLabelBuddy(QDialog):
    def __init__(self):
        super().__init__()
        self.resize(220, 200)
        self.setWindowIcon(QIcon("./dz.png"))
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('QLabel与伙伴控件')
        nameLabel = QLabel('&Name', self)
        nameLineEdit = QLineEdit(self)
        # 设置伙伴控件
        nameLabel.setBuddy(nameLineEdit)
        passwordLabel = QLabel('&Password', self)
        passwordLineEdit = QLineEdit(self)
        # 设置伙伴控件
        passwordLabel.setBuddy(passwordLineEdit)
        btnOK = QPushButton('&OK')
        btnCancel = QPushButton('&Cancel')
        btnOK.clicked.connect(btn_ok)
        btnCancel.clicked.connect(btn_cancel)

        mainLayout = QGridLayout(self)
        mainLayout.addWidget(nameLabel, 0, 0)
        mainLayout.addWidget(nameLineEdit, 0, 1, 1, 2)
        mainLayout.addWidget(passwordLabel, 1, 0)
        mainLayout.addWidget(passwordLineEdit, 1, 1, 1, 2)
        mainLayout.addWidget(btnOK, 2, 1)
        mainLayout.addWidget(btnCancel, 2, 2)


def btn_ok(self):
    print('---ok----')


def btn_cancel(self):
    print('---cancel----')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLabelBuddy()
    main.show()
    sys.exit(app.exec_())