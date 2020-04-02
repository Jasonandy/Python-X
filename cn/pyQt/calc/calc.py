import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow


class Calc(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.x = None
        self.y = None
        self.result = None
        self.operator = None
        self.equal = None

        uic.loadUi('calc.ui', self)
        btns = [
            self.pushButton0,
            self.pushButton1,
            self.pushButton2,
            self.pushButton3,
            self.pushButton4,
            self.pushButton5,
            self.pushButton6,
            self.pushButton7,
            self.pushButton8,
            self.pushButton9,
            self.pushButton_clear,
            self.pushButton_add,
            self.pushButton_sub,
            self.pushButton_div,
            self.pushButton_mul,
            self.pushButton_dot,
            self.pushButton_equal
        ]

        for btn in btns:
            btn.clicked.connect(self.click_on_button)

    def calculate(self):
        """
        如果x、y、operater不为空，计算结果,计算出结果后，清空y,保持x和结果相等。
        """
        if self.x and self.y and self.operator:
            s = "%s%s%s" % (self.x, self.operator, self.y)
            print
            s
            self.x = self.result = str(eval(s))
            self.y = None
            self.text_result.setText(self.result)

    def click_on_button(self):

        print
        "点击按钮前：", self.x, self.operator, self.y
        value = self.sender().text()

        # 点击数字的处理：
        # 1   点数字时，无运算符且有x，累加x
        # 2   点数字时，有运算符且有y，累加y
        # 3   点数字时，无运算符且无x，赋值给x
        # 4   点数字时，有运算符且无Y，赋值给y

        if value in "0123456789.":
            if self.operator is not None:  # 有运算符
                if self.y is not None:  # 有y
                    self.y = self.y + value
                else:  # 无y
                    if value != '0':
                        self.y = value
                if self.y is not None:
                    self.text_result.setText(self.y)

            else:  # 无运算符
                if self.x is not None:  # 有x
                    self.x = self.x + value

                else:
                    if value != '0':
                        self.x = value
                if self.x is not None:
                    self.text_result.setText(self.x)


        # 开始处理运算符
        # 1.点运算符时记录运算符
        # 2.点运算符时计算结果，然后记录运算符(x,y,oper都有值)
        # 2.点运算符时记录运算符并计算结果(x,y,oper都有值)
        # 3.点运算符时记录运算符，并将x置为0(x无值)

        elif value in "+-*/":

            if self.x is None:
                self.x = '0'
            if self.x and self.y and self.operator:
                self.calculate()
            self.operator = value

        # 处理点击等号的操作
        # 1.点等号时计算结果 (x,y,oper都有值）
        # 2.点等号时忽略等号 (x,y,oper不都有值)

        elif value == "=":
            if self.x and self.y and self.operator:
                self.calculate()

        else:
            print("您点击的是C")
            self.clear()
        print("点击按钮后：", self.x, self.operator, self.y)

    def clear(self):
        self.x = None
        self.y = None
        self.result = None
        self.operator = None
        self.text_result.setText("")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calc()
    calc.show()
    app.exec_()