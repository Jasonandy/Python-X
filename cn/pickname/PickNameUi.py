# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PickNameUi.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actiondaoru = QtWidgets.QAction(MainWindow)
        self.actiondaoru.setObjectName("actiondaoru")
        self.actionqingkong = QtWidgets.QAction(MainWindow)
        self.actionqingkong.setObjectName("actionqingkong")
        self.actionruanjian = QtWidgets.QAction(MainWindow)
        self.actionruanjian.setObjectName("actionruanjian")
        self.actionzuozhe = QtWidgets.QAction(MainWindow)
        self.actionzuozhe.setObjectName("actionzuozhe")
        self.menu.addSeparator()
        self.menu.addAction(self.actiondaoru)
        self.menu.addSeparator()
        self.menu.addAction(self.actionqingkong)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.actionruanjian)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.actionzuozhe)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menu.setTitle(_translate("MainWindow", "设置"))
        self.menu_2.setTitle(_translate("MainWindow", "关于作者"))
        self.actiondaoru.setText(_translate("MainWindow", "导入数据"))
        self.actionqingkong.setText(_translate("MainWindow", "清空数据"))
        self.actionruanjian.setText(_translate("MainWindow", "软件信息 "))
        self.actionruanjian.setStatusTip(_translate("MainWindow", "查看软件信息"))
        self.actionruanjian.setWhatsThis(_translate("MainWindow", "点击查看软件信息"))
        self.actionzuozhe.setText(_translate("MainWindow", "作者信息"))
