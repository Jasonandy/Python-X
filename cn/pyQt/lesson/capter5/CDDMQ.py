# -*- coding: utf-8 -*-
import os
import random

from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from PyQt5.QtCore import QDateTime, QTimer
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel
from PyQt5.QtWidgets import QLabel, QMessageBox, QFileDialog


"""
注释:

"""
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        # 创建主窗口
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(621, 372)

        # 窗口布局
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # 设置下拉框 复选框
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(50, 50, 69, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("2001")
        self.comboBox.addItem("2002")
        self.comboBox.addItem("2003")
        self.comboBox.addItem("2004")

        # 按钮 01 开始点名
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 300, 75, 23))
        self.pushButton.setObjectName("pushButton")

        # 按钮 02 结束点名
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 300, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        # 文本框 显示 被点名点中的学生
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(40, 90, 256, 192))
        self.textBrowser.setObjectName("textBrowser")

        # 状态栏 “幸运学生”
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 50, 71, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setOpenExternalLinks(False)
        self.label_2.setObjectName("label_2")

        # 创建时间空间 显示时间
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(340, 90, 248, 197))
        self.calendarWidget.setObjectName("calendarWidget")
        MainWindow.setCentralWidget(self.centralwidget)


        # 菜单栏 工具条
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 621, 23))
        self.menubar.setObjectName("menubar")

        # 菜单栏 创建菜单
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")

        # 菜单栏 2
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")

        # 祝窗口 设置 菜单栏
        MainWindow.setMenuBar(self.menubar)

        # 设置状态栏 实时显示状态
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # action控制
        self.actionruanjian_xixin = QtWidgets.QAction(MainWindow)
        # 软件信息
        self.actionruanjian_xixin.setObjectName("actionruanjian_xixin")

        # action控制 版本信息
        self.action_version_info = QtWidgets.QAction(MainWindow)
        # 软件信息
        self.action_version_info.setObjectName("action_version_info")

        # 导入控制
        self.actiondaoru = QtWidgets.QAction(MainWindow)
        self.actiondaoru.setObjectName("actiondaoru")
        # 设置导入快捷键
        self.actiondaoru.setShortcut("Ctrl + i")

        # 数据清空
        self.action_clear_data = QtWidgets.QAction(MainWindow)
        self.action_clear_data.setObjectName("action_clear_data")

        self.menu.addSeparator()

        # 菜单栏01 添加一个动作 （导入）
        self.menu.addAction(self.actiondaoru)
        # 01 数据清空
        self.menu.addAction(self.action_clear_data)

        # 菜单栏02
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.actionruanjian_xixin)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.action_version_info)

        #  菜单条 -- 菜单列 --动作
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        # 软件信息 动作
        self.actionruanjian_xixin.triggered.connect(self.soft_info)

        # 版本信息 动作
        self.action_version_info.triggered.connect(self.version_info)

        self.actiondaoru.triggered.connect(self.import_class_info)
        self.action_clear_data.triggered.connect(self.clear_class_info)

        self.retranslateUi(MainWindow)

        # btn 1 开始按钮
        self.pushButton.clicked.connect(self.choose_name_start)
        # btn 2 结束按钮
        self.pushButton_2.clicked.connect(self.choose_name_end)

        self.label = QLabel(self.centralwidget)
        self.label.setText(QDateTime.currentDateTime().toString("yyyy-MM-dd HH:ss:mm"))
        self.label.move(500, 10)

        # 全局的定时器
        self.timer = QTimer(self.centralwidget)

        self.stu_name_list = []

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def soft_info(self):
        QtWidgets.QMessageBox.about(self.centralwidget, '作者信息', '<font color="blue">勿忘初心 放得始终 </font> '
                                                                '<br/> Powered  by  <br/> '
                                                                '<font color="red">佛系小吴</font>'
                                                                '<br/> 湘北名校 楚雄中学')

    def version_info(self):
        QtWidgets.QMessageBox.about(self.centralwidget, '版本信息', '<font color="blue"> Version: V1.0 </font> '
                                                                '<br/> Release Time <br/> '
                                                                '<font color="red">2020-12-26</font>')

    def clear_class_info(self):
        print('数据清空')
        db = QSqlDatabase.addDatabase('QSQLITE')
        # 指定SQLite数据库的文件名
        db.setDatabaseName('./class_info.db')
        if not db.open():
            print('无法建立与数据库的连接')
            return False
        query = QSqlQuery()
        clear_stu_info_str = 'delete from people'
        clear_flag = query.exec(clear_stu_info_str)
        db.close()
        if clear_flag:
            print('清空完成')


    def import_class_info(self):
        txt_file_name, _ = QtWidgets.QFileDialog.getOpenFileName(self.centralwidget, '导入班级信息到数据库', '.',
                                                                 '文本文件(*.txt *.json)')
        db = QSqlDatabase.addDatabase('QSQLITE')
        # 指定SQLite数据库的文件名
        db.setDatabaseName('./class_info.db')
        if not db.open():
            print('无法建立与数据库的连接')
            return False
        query = QSqlQuery()
        # xxx /2001.txt
        #file_name = txt_file_name.split(".", 2)
        txt_file_name_list = txt_file_name.split("/")
        txt_file_name_class = txt_file_name_list[-1].split(".")[0]
        print(txt_file_name_list[-1].split(".")[0])
        # 将文本里的数据 逐行读取 然后存入sql.lite数据库
        for line in open(txt_file_name):
            insert_stu_info_str = 'insert into people values'+'(NULL,'+line+','+txt_file_name_class+')'
            query.exec(insert_stu_info_str)
            print(insert_stu_info_str)
        db.close()

    def choose_name_start(self):
        # 对文本进行处理 - 存入 sql_lite 数据库
        flag = self.create_db()
        if flag == True:
            print("数据创建成功！")
        self.view_data()
        print('开始点名')


    # 结束点名
    def choose_name_end(self):
        self.timer.stop()
        print('结束点名')


    # 创建SQL_lite 数据库
    def create_db(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        # 指定SQLite数据库的文件名
        db.setDatabaseName('./class_info.db')
        if not db.open():
            print('无法建立与数据库的连接')
            return False
        query = QSqlQuery()
        query.exec('create table people(id  INTEGER PRIMARY KEY AUTOINCREMENT,name varchar(10),class_no varchar(50))')
        db.close()
        return True

    def view_data(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        # 指定SQLite数据库的文件名
        db.setDatabaseName('./class_info.db')
        if not db.open():
            print('无法建立与数据库的连接')
            return False
        q = QSqlQuery()

        # 查询选中的班级
        class_index_str = self.comboBox.currentText()
        print('选中的班级为 %s ' % class_index_str)

        # 清空一下数据 避免重复添加的问题
        self.stu_name_list.clear()
       # sql_code = 'select * from people where class_no ='+class_index_str +' order by random() limit 1'
        # 优化一下  查询出所有的数据 封装成 list 然后 随机取出数据 显示
        sql_code = 'select * from people where class_no =' + class_index_str
        if True:
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
            self.start_show_name()
        db.close()

    # 将名字赋值进去
    def set_stu_name(self):
        if len(self.stu_name_list) != 0:
            name = self.stu_name_list[random.randint(0, len(self.stu_name_list) - 1)]
            self.textBrowser.setText("恭喜<font size='32' color='red'>"+name+"</font>同学")
        else:
            return False

    # 实现定时不断的刷新
    def start_show_name(self):
        print('start_show_name')
        self.timer.timeout.connect(self.set_stu_name)
        self.timer.start(100)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox.setItemText(0, _translate("MainWindow", "2001"))
        self.comboBox.setItemText(1, _translate("MainWindow", "2002"))
        self.comboBox.setItemText(2, _translate("MainWindow", "2003"))
        self.comboBox.setItemText(3, _translate("MainWindow", "2004"))
        self.pushButton.setText(_translate("MainWindow", "开始点名"))
        self.pushButton_2.setText(_translate("MainWindow", "暂停"))
        self.textBrowser.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "幸运学生"))
        self.menu.setTitle(_translate("MainWindow", "设置"))
        self.menu_2.setTitle(_translate("MainWindow", "关于"))
        self.action_version_info.setText(_translate("MainWindow", "版本信息"))
        self.actionruanjian_xixin.setText(_translate("MainWindow", "软件信息"))
        self.actiondaoru.setText(_translate("MainWindow", "数据导入"))
        self.actiondaoru.setToolTip(_translate("MainWindow", "导入班级信息数据"))
        self.action_clear_data.setText(_translate("MainWindow", "数据清空"))
        self.action_clear_data.setToolTip(_translate("MainWindow", "清空数据库"))

