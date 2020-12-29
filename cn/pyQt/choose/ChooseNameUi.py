from PyQt5.QtWidgets import QLabel, QLineEdit, QGridLayout
from qtpy import QtCore, QtWidgets


class ChooseNameMainUi(object):
    """
      点名器ui
    """
    def __init__(self, choose_name_main_window):
        """
           设置初始化
           :param choose_name_main_window:
           :return:
       """
        print("--- set_up ---")
        # 设置主窗口
        choose_name_main_window.setObjectName("choose_name_main_window_name")
        # 窗口布局
        self.grid_layout = QGridLayout(choose_name_main_window)
        # 设置布局的名字
        self.grid_layout.setObjectName("choose_name_grid_layout_name")

        # 设置下拉框 复选框
        self.class_combo_box = QtWidgets.QComboBox(choose_name_main_window)
        self.class_combo_box.setGeometry(QtCore.QRect(20, 20, 50, 50))
        self.class_combo_box.setObjectName("class_combo_box_name")
        self.class_combo_box.addItem("2001")
        self.class_combo_box.addItem("2002")
        self.class_combo_box.addItem("2003")
        self.class_combo_box.addItem("2004")

        # 菜单条
        self.menu_bar = QtWidgets.QMenuBar(choose_name_main_window)
        self.menu_bar.setObjectName("menu_bar_name")

        # action控制
        self.action_author_info = QtWidgets.QAction(choose_name_main_window)
        # 软件信息
        self.action_author_info.setObjectName("action_author_info_name")


        # 菜单状态栏 - 设置
        self.menu_1 = QtWidgets.QMenu(self.menu_bar)
        self.menu_1.setObjectName("menu_1_name")

        # 菜单栏01
        self.menu_1.addSeparator()
        self.menu_1.addAction(self.action_author_info)
        self.menu_1.addSeparator()
        self.menu_1.addAction(self.action_author_info)

        # 菜单状态栏 - 关于
        self.menu_2 = QtWidgets.QMenu(self.menu_bar)
        self.menu_2.setObjectName("menu_2_name")

        # 菜单栏02
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.action_author_info)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.action_author_info)



        #  菜单条 -- 菜单列 --动作
        self.menu_bar.addAction(self.menu_1.menuAction())
        self.menu_bar.addAction(self.menu_2.menuAction())



        # 主窗口显示菜单条
        choose_name_main_window.setMenuBar(self.menu_bar)


        self.title = QLabel('Title')
        self.title_edit = QLineEdit(choose_name_main_window)
        self.grid_layout.setSpacing(10)

        self.grid_layout.addWidget(self.title, 1, 0)
        self.grid_layout.addWidget(self.title_edit, 1, 1)

        self.grid_layout.addWidget(self.menu_bar)

        # 设置主窗口信息
        self.re_translate_ui(choose_name_main_window)




    def re_translate_ui(self, choose_name_main_window):
        """
        解析ui
        :param choose_name_main_window:
        :return: 解析ui界面文件
        """
        _translate = QtCore.QCoreApplication.translate
        choose_name_main_window.setWindowTitle(_translate("choose_name_main_window_name", "choose_name_main_window"))
        choose_name_main_window.setWindowTitle(_translate("class_combo_box_name", "choose_name_main_window"))
        self.action_author_info.setText(_translate("choose_name_main_window_name", "作者信息"))
        self.action_author_info.setText(_translate("choose_name_main_window_name", "作者信息"))

