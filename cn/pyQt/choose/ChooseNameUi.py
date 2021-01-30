import random

from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QIcon
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtWidgets import QLabel, QLineEdit, QGridLayout, QMenuBar, QComboBox, QMenu, QAction, QMessageBox, \
    QPushButton, QTextBrowser
from qtpy import QtCore, QtWidgets, QtGui


class ChooseNameMainUi(object):
    """
      点名器ui
    """
    def __init__(self, choose_name_main_window):
        """
           设置初始化
           :param choose_name_main_window: 主窗口对象
           :return:
       """
        print("--- set_up ---")
        self.main_window = choose_name_main_window
        # 设置主窗口
        choose_name_main_window.setObjectName("choose_name_main_window_name")
        # 窗口布局
        self.grid_layout = QGridLayout(choose_name_main_window)
        # 设置布局的名字
        self.grid_layout.setObjectName("choose_name_grid_layout_name")

        self.label_class_info = QLabel(choose_name_main_window)
        self.label_class_info.setGeometry(QtCore.QRect(140, 50, 80, 35))
        self.label_class_info.setTextFormat(QtCore.Qt.AutoText)
        self.label_class_info.setOpenExternalLinks(False)
        self.label_class_info.setObjectName("label_class_info_name")
        self.label_class_info.setStyleSheet("color:red;")



        # 按钮 01 开始点名
        self.push_btn_start = QPushButton(choose_name_main_window)
        self.push_btn_start.setGeometry(QtCore.QRect(60, 300, 60, 60))
        self.push_btn_start.setStyleSheet("QPushButton:pressed{border-image: url(./img/tag/start_btn.svg)}")
        self.push_btn_start.setObjectName("push_btn_start_name")

        # 按钮 02 暂停点名
        self.push_btn_pause = QPushButton(choose_name_main_window)
        self.push_btn_pause.setGeometry(QtCore.QRect(350, 300, 60, 60))
        self.push_btn_pause.setStyleSheet("QPushButton:pressed{border-image: url(./img/tag/end_btn.svg)}")
        self.push_btn_pause.setObjectName("push_btn_pause_name")


        self.grid_layout.addWidget(self.label_class_info, 1, 4)
        self.grid_layout.addWidget(self.push_btn_start, 10, 1)
        self.grid_layout.addWidget(self.push_btn_start, 10, 2)

        # btn 1 开始按钮
        self.push_btn_start.clicked.connect(self.fun_push_btn_start)
        # btn 2 暂停按钮
        self.push_btn_pause.clicked.connect(self.fun_push_btn_pause)


        # 文本框 显示 被点名点中的学生
        self.text_name_show = QTextBrowser(choose_name_main_window)
        self.text_name_show.setGeometry(QtCore.QRect(40, 90, 256, 192))
        self.text_name_show.setObjectName("text_name_show_name")
        #self.text_name_show.setStyleSheet("background-color: green;")

        # 设置下拉框 复选框
        self.class_combo_box = QComboBox(choose_name_main_window)
        self.class_combo_box.setGeometry(QtCore.QRect(40, 40, 60, 20))
        self.class_combo_box.setObjectName("class_combo_box_name")
        self.class_combo_box.addItem("2001")
        self.class_combo_box.addItem("2002")
        self.class_combo_box.addItem("2003")
        self.class_combo_box.addItem("2004")

        # 菜单条
        self.menu_bar = QMenuBar(choose_name_main_window)
        self.menu_bar.setObjectName("menu_bar_name")

        # 作者信息
        self.action_author_info = QAction(choose_name_main_window)
        self.action_author_info.setObjectName("action_author_info_name")

        # 软件信息
        self.action_software_info = QAction(choose_name_main_window)
        self.action_software_info.setObjectName("action_software_info_name")

        # 导入班级数据
        self.action_import_class_info = QAction(choose_name_main_window)
        self.action_import_class_info.setObjectName("action_import_class_info_name")

        # 清空数据
        self.action_null_class_info = QAction(choose_name_main_window)
        self.action_null_class_info.setObjectName("action_null_class_info_name")

        # 菜单状态栏 - 设置
        self.menu_1 = QMenu(self.menu_bar)
        self.menu_1.setObjectName("menu_1_name")

        # 菜单栏01
        self.menu_1.addSeparator()
        self.menu_1.addAction(self.action_import_class_info)
        self.menu_1.addSeparator()
        self.menu_1.addAction(self.action_null_class_info)

        # 菜单状态栏 - 关于
        self.menu_2 = QMenu(self.menu_bar)
        self.menu_2.setObjectName("menu_2_name")

        # 绑定信号与槽
        self.action_import_class_info.triggered.connect(self.fun_import_class_info)
        self.action_null_class_info.triggered.connect(self.fun_null_class_info)
        self.action_software_info.triggered.connect(self.fun_software_info)
        self.action_author_info.triggered.connect(self.fun_author_info)

        # 菜单栏02
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.action_software_info)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.action_author_info)

        #  菜单条 -- 菜单列 --动作
        self.menu_bar.addAction(self.menu_1.menuAction())
        self.menu_bar.addAction(self.menu_2.menuAction())

        # 主窗口显示菜单条
        choose_name_main_window.setMenuBar(self.menu_bar)

        # 设置主窗口信息
        self.re_translate_ui(choose_name_main_window)

        # 全局的定时器
        self.choose_name_timer = QTimer(choose_name_main_window)

        # 数据库查询到数据 然后随机匹配
        self.stu_name_list = ['无名英雄']

    def fun_push_btn_start(self):
        self.select_db_data()
        print("开始按钮")

    def fun_push_btn_pause(self):
        self.choose_name_timer.stop()
        print("暂停按钮")


    def select_db_data(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        # 指定SQLite数据库的文件名
        db.setDatabaseName('./db/database.db')
        if not db.open():
            print('无法建立与数据库的连接')
            return False
        q = QSqlQuery()

        # 查询选中的班级
        class_index_str = self.class_combo_box.currentText()
        print('选中的班级为 %s ' % class_index_str)
        # 清空一下数据 避免重复添加的问题
        self.stu_name_list.clear()
        # 优化一下  查询出所有的数据 封装成 list 然后 随机取出数据 显示
        sql_code = 'select * from people where class_no =' + class_index_str
        if len(self.stu_name_list) != 0:
            q.exec_(sql_code)
            id_index = q.record().indexOf('id')
            name_index = q.record().indexOf('name')
            class_index = q.record().indexOf('class_no')
            while q.next():
                student_name = q.value(name_index)
                student_class = q.value(class_index)
                student_id = q.value(id_index)
                print(student_name, student_class, student_id)
                self.stu_name_list.append(student_name)
            self.fun_start_loop_name()
        db.close()
        self.text_name_show.setText("本系统暂时未录入数据，请先录入数据!")

    def fun_import_class_info(self):
        txt_file_name, ok = QtWidgets.QFileDialog.getOpenFileName(self.main_window, '导入班级信息到数据库', '.',
                                                                 '文本文件(*.txt)')
        db = QSqlDatabase.addDatabase('QSQLITE')
        # 指定SQLite数据库的文件名
        db.setDatabaseName('./db/database.db')
        if not db.open():
            print('无法建立与数据库的连接')
            return False
        db_flag = self.crate_sql_lite_db()
        if db_flag:
            query = QSqlQuery()
            # xxx /2001.txt
            # file_name = txt_file_name.split(".", 2)
            txt_file_name_list = txt_file_name.split("/")
            txt_file_name_class = txt_file_name_list[-1].split(".")[0]
            print(txt_file_name_list[-1].split(".")[0])
            if ok:
                # 将文本里的数据 逐行读取 然后存入sql.lite数据库, encoding='utf-8'
                for line in open(txt_file_name, encoding='utf-8'):
                    insert_stu_info_str = 'insert into people values' + '(NULL,"' + str(line) + '",'\
                                          + txt_file_name_class + ')'
                    query.exec(insert_stu_info_str)
                    print(insert_stu_info_str)
                db.close()
                print("导入班级信息")
        else:
            return False

    # 创建SQL_lite 数据库
    def crate_sql_lite_db(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        # 指定SQLite数据库的文件名
        db.setDatabaseName('./db/database.db')
        if not db.open():
            print('无法建立与数据库的连接')
            return False
        query = QSqlQuery()
        query.exec(
            'create table people(id  INTEGER PRIMARY KEY AUTOINCREMENT,name varchar(50),class_no varchar(50))')
        db.close()
        return True

    def clear_class_info(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        # 指定SQLite数据库的文件名
        db.setDatabaseName('./db/database.db')
        if not db.open():
            print('无法建立与数据库的连接')
            return False
        query = QSqlQuery()
        clear_stu_info_str = 'delete from people'
        clear_flag = query.exec(clear_stu_info_str)
        db.close()
        if clear_flag:
            print('清空完成')
        else:
            print('清除失败')

    def fun_null_class_info(self):
        self.clear_class_info()



    # 实现定时不断的刷新
    def fun_start_loop_name(self):
        print('fun_start_loop_name')
        self.choose_name_timer.timeout.connect(self.fun_show_stu_name)
        self.choose_name_timer.start(150)

    def fun_show_stu_name(self):
        print('fun_show_stu_name')
        if len(self.stu_name_list) != 0:
            name = self.stu_name_list[random.randint(0, len(self.stu_name_list) - 1)]
            sign = str("<font size='36' color='red'>恭喜<br/>%s<br/>同学</font>" % name)
            self.text_name_show.setText(sign)
        else:
            return False

    def fun_software_info(self):
        print("查看软件信息")
        QMessageBox.about(self.main_window, '软件信息', '<font color="blue"> Version: V1.0 </font> <br/>'
                                                        '<font color="red">Based on PyQt5 </font><br/>'
                                                        '<font color="black">jasonandy@hotmail.com</font>')

    def fun_author_info(self):
        print("查看作者信息")
        QMessageBox.about(self.main_window, '作者信息', '<font color="blue">勿忘初心 放得始终 </font> '
                                                                '<br/> Powered  by  <br/> '
                                                                '<font color="red">佛系小吴</font>'
                                                                '<br/> 湘北名校 楚雄中学')




    def re_translate_ui(self, choose_name_main_window):
        """
        解析ui
        :param choose_name_main_window:
        :return: 解析ui界面文件
        """
        _translate = QtCore.QCoreApplication.translate
        choose_name_main_window.setWindowTitle(_translate("choose_name_main_window_name", "choose_name_main_window"))
        choose_name_main_window.setWindowTitle(_translate("choose_name_main_window_name", "choose_name_main_window"))
        self.menu_1.setTitle(_translate("choose_name_main_window_name", "设置"))
        self.menu_2.setTitle(_translate("choose_name_main_window_name", "关于"))
        self.action_author_info.setText(_translate("choose_name_main_window_name", "作者信息"))
        self.action_software_info.setText(_translate("choose_name_main_window_name", "软件信息"))
        self.action_import_class_info.setText(_translate("choose_name_main_window_name", "导入数据"))
        self.action_null_class_info.setText(_translate("choose_name_main_window_name", "清空数据"))
        self.label_class_info.setText(_translate("choose_name_main_window_name", "幸运学生"))
        self.push_btn_start.setText(_translate("choose_name_main_window_name", "Start"))
        self.push_btn_pause.setText(_translate("choose_name_main_window_name", "Pause"))
