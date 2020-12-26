'''
QLabel控件
setAlignment()：设置文本的对齐方式
setIndent()：设置文本缩进
text()：获取文本内容
setBuddy()：设置伙伴关系
setText()：设置文本内容
selectedText()：返回所选择的字符
setWordWrap()：设置是否允许换行
QLabel常用的信号（事件）：
1.  当鼠标滑过QLabel控件时触发：linkHovered
2.  当鼠标单击QLabel控件时触发：linkActivated
'''

import sys
from PyQt5.QtWidgets import QVBoxLayout, QApplication, QLabel, QWidget
from PyQt5.QtGui import QPixmap, QPalette, QIcon
from PyQt5.QtCore import Qt


class QLabelDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('./dz.png'))
        self.resize(400, 500)
        self.init_ui()

    def init_ui(self):
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        label1.setText("<font color='yellow' size='32'>这是一个文本标签.</font>")
        # 自动填充背景
        label1.setAutoFillBackground(True)
        # 调色板
        palette = QPalette()
        palette.setColor(QPalette.Window, Qt.red)  # 设置背景色
        label1.setPalette(palette)
        # 设置 居中
        label1.setAlignment(Qt.AlignCenter)

        label2.setText("<a href='#'> <font color='red'> 勿忘初心 放得始终</font></a>")

        label3.setAlignment(Qt.AlignCenter)

        label3.setToolTip('This is  a 图片标签')
        # 设置pix map
        label3.setPixmap(QPixmap("./zb.png"))

        # 如果设为True，用浏览器打开网页，如果设为False，调用槽函数
        label4.setOpenExternalLinks(True)

        label4.setText("<a href='https://www.baidu.com'>感谢关注《佛系小吴》</a>")

        label4.setAlignment(Qt.AlignRight)

        label4.setToolTip('佛系小吴Blog')

        # 垂直布局
        vbox = QVBoxLayout()

        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)

        # 时间绑定到函数  （信号与槽绑定 ）
        label2.linkHovered.connect(self.linkHovered)
        label4.linkActivated.connect(self.linkClicked)

        self.setLayout(vbox)
        self.setWindowTitle('QLabel控件演示')

    def linkHovered(self):
        print('当鼠标滑过label2标签时，触发事件')

    def linkClicked(self):
        print('当鼠标单击label4标签时，触发事件')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLabelDemo()
    main.show()
    sys.exit(app.exec_())