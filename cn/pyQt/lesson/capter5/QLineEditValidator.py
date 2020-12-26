'''
现在QLineEdit控件的输入（校验器）
如限制只能输入整数、浮点数或满足一定条件的字符串
'''

from PyQt5.QtWidgets import QApplication, QFormLayout, QLineEdit, QWidget
from PyQt5.QtGui import QIcon, QIntValidator, QDoubleValidator, QRegExpValidator
from PyQt5.QtCore import QRegExp
import sys


class QLineEditValidator(QWidget):
    def __init__(self):
        super(QLineEditValidator,self).__init__()
        self.resize(300, 100)
        self.setWindowIcon(QIcon('./tx.png'))
        self.initUI()

    def initUI(self):
        self.setWindowTitle('校验器')

        # 创建表单布局
        form_lay_out = QFormLayout()

        int_line_edit = QLineEdit()
        double_line_edit = QLineEdit()
        validator_line_edit = QLineEdit()

        form_lay_out.addRow('整数类型', int_line_edit)
        form_lay_out.addRow('浮点类型', double_line_edit)
        form_lay_out.addRow('数字和字母', validator_line_edit)

        int_line_edit.setPlaceholderText('整型')
        double_line_edit.setPlaceholderText('浮点型')
        validator_line_edit.setPlaceholderText('字母和数字')

        # 整数校验器 [1,99]
        int_validator = QIntValidator(self)
        int_validator.setRange(1, 99)

        # 浮点校验器 [-360,360]，精度：小数点后2位
        double_validator = QDoubleValidator(self)
        double_validator.setRange(-360, 360)
        double_validator.setNotation(QDoubleValidator.StandardNotation)
        # 设置精度，小数点2位
        double_validator.setDecimals(2)

        # 字符和数字
        reg = QRegExp('[a-zA-z0-9]+$')
        reg_validator = QRegExpValidator(self)
        reg_validator.setRegExp(reg)

        # 设置校验器

        int_line_edit.setValidator(int_validator)
        double_line_edit.setValidator(double_validator)
        validator_line_edit.setValidator(reg_validator)

        self.setLayout(form_lay_out)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLineEditValidator()
    main.show()
    sys.exit(app.exec_())