from PyQt5.QtWidgets import QApplication, QFormLayout, QWidget, QLineEdit
from PyQt5.QtGui import QIcon
import sys

'''
QLineEdit控件与回显模式
基本功能：输入单行的文本
EchoMode（回显模式）
4种回显模式
1. Normal 正常
2. NoEcho 不回显   什么也不出现
3. Password 密码 一直是隐藏
4. PasswordEchoOnEdit 编辑的时候是显示  不编辑的时候 隐藏
Mac : Command    Windows:Control
'''
class QLineEditEchoMode(QWidget) :
    def __init__(self):
        super(QLineEditEchoMode, self).__init__()
        self.resize(300, 150)
        self.setWindowIcon(QIcon('./tx.png'))
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('回显模式')

        # 表单布局
        form_layout = QFormLayout()
        normal_line_edit = QLineEdit()
        no_echo_line_edit = QLineEdit()
        password_line_edit = QLineEdit()
        password_echo_on_edit_line_edit = QLineEdit()

        form_layout.addRow("Normal", normal_line_edit)
        form_layout.addRow("NoEcho", no_echo_line_edit)
        form_layout.addRow("Password", password_line_edit)
        form_layout.addRow("PasswordEchoOnEdit", password_echo_on_edit_line_edit)

        # 设置 提示占位符
        normal_line_edit.setPlaceholderText("Normal")
        no_echo_line_edit.setPlaceholderText("NoEcho")
        password_line_edit.setPlaceholderText("Password")
        password_echo_on_edit_line_edit.setPlaceholderText("PasswordEchoOnEdit")

        normal_line_edit.setEchoMode(QLineEdit.Normal)
        no_echo_line_edit.setEchoMode(QLineEdit.NoEcho)
        password_line_edit.setEchoMode(QLineEdit.Password)
        password_echo_on_edit_line_edit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.setLayout(form_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLineEditEchoMode()
    main.show()
    sys.exit(app.exec_())