# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inquire.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Inquire(object):
    def setupUi(self, Inquire):
        Inquire.setObjectName("Inquire")
        Inquire.resize(782, 754)
        self.centralwidget = QtWidgets.QWidget(Inquire)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(70, 90, 241, 71))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineName = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineName.setFont(font)
        self.lineName.setObjectName("lineName")
        self.horizontalLayout.addWidget(self.lineName)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(440, 90, 241, 71))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_11 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_4.addWidget(self.label_11)
        self.linePhone = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.linePhone.setFont(font)
        self.linePhone.setObjectName("linePhone")
        self.horizontalLayout_4.addWidget(self.linePhone)
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(70, 180, 351, 71))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_13 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_6.addWidget(self.label_13)
        self.lineIdcard = QtWidgets.QLineEdit(self.horizontalLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineIdcard.setFont(font)
        self.lineIdcard.setObjectName("lineIdcard")
        self.horizontalLayout_6.addWidget(self.lineIdcard)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(280, 10, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(70, 270, 661, 321))
        self.tableView.setObjectName("tableView")
        self.RButtonYes = QtWidgets.QPushButton(self.centralwidget)
        self.RButtonYes.setGeometry(QtCore.QRect(160, 610, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.RButtonYes.setFont(font)
        self.RButtonYes.setObjectName("RButtonYes")
        self.RButtonOut = QtWidgets.QPushButton(self.centralwidget)
        self.RButtonOut.setGeometry(QtCore.QRect(440, 610, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.RButtonOut.setFont(font)
        self.RButtonOut.setObjectName("RButtonOut")
        Inquire.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Inquire)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 782, 25))
        self.menubar.setObjectName("menubar")
        Inquire.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Inquire)
        self.statusbar.setObjectName("statusbar")
        Inquire.setStatusBar(self.statusbar)

        self.retranslateUi(Inquire)
        QtCore.QMetaObject.connectSlotsByName(Inquire)

    def retranslateUi(self, Inquire):
        _translate = QtCore.QCoreApplication.translate
        Inquire.setWindowTitle(_translate("Inquire", "MainWindow"))
        self.label.setText(_translate("Inquire", "名字"))
        self.label_11.setText(_translate("Inquire", "手机"))
        self.label_13.setText(_translate("Inquire", "身份证"))
        self.label_2.setText(_translate("Inquire", "检索条件"))
        self.RButtonYes.setText(_translate("Inquire", "确定"))
        self.RButtonOut.setText(_translate("Inquire", "退出"))

