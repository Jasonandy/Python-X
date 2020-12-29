import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow

from pyQt.choose.ChooseNameUi import ChooseNameMainUi


class ChooseName(QMainWindow):
    """
    ChooseName 继承 QMainWindow
    点名器 - 楚雄中学课堂点名器
    """
    def __init__(self):
        super(ChooseName, self).__init__()
        self.init_ui()

    def init_ui(self):
        """
        初始化 ui
        :return:
        """
        print('--- init main ---')


if __name__ == '__main__':
    """
        主函数入口
    """
    app = QApplication(sys.argv)
    # 初始化 程序 QMainWindow
    choose_name_main_window = ChooseName()
    # ChooseNameMainUi 所有的ui布局
    main_ui = ChooseNameMainUi(choose_name_main_window)
    # 将主窗口函数传入 初始化函数
    # main_ui.set_up_ui(choose_name_main_window)
    # 设置窗口坐标
    # self.setGeometry(300, 300, 250, 250)
    choose_name_main_window.resize(600, 400)
    # 设置主窗口的标题
    choose_name_main_window.setWindowTitle('楚大点名器   --- 湘北名校 楚雄中学 Made by 佛系小吴')
    # 设置窗口图标
    choose_name_main_window.setWindowIcon(QIcon('./img/icon/logo.svg'))
    # show 显示窗口
    choose_name_main_window.show()
    sys.exit(app.exec_())

