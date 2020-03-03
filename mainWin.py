# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWin.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_JD(object):
    def setupUi(self, JD):
        JD.setObjectName("JD")
        JD.setWindowModality(QtCore.Qt.ApplicationModal)
        JD.resize(791, 591)
        self.timeLabel = QtWidgets.QLabel(JD)
        self.timeLabel.setGeometry(QtCore.QRect(510, 560, 261, 21))
        self.timeLabel.setObjectName("timeLabel")
        self.line_4 = QtWidgets.QFrame(JD)
        self.line_4.setGeometry(QtCore.QRect(20, 10, 751, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line = QtWidgets.QFrame(JD)
        self.line.setGeometry(QtCore.QRect(10, 20, 20, 531))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(JD)
        self.line_2.setGeometry(QtCore.QRect(20, 540, 751, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(JD)
        self.line_3.setGeometry(QtCore.QRect(760, 20, 20, 531))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.log_terminal = QtWidgets.QTextBrowser(JD)
        self.log_terminal.setGeometry(QtCore.QRect(40, 371, 711, 161))
        self.log_terminal.setObjectName("log_terminal")
        self.LoginBtn = QtWidgets.QPushButton(JD)
        self.LoginBtn.setGeometry(QtCore.QRect(50, 170, 201, 28))
        self.LoginBtn.setObjectName("LoginBtn")
        self.usernameLabel = QtWidgets.QLabel(JD)
        self.usernameLabel.setGeometry(QtCore.QRect(50, 120, 101, 21))
        self.usernameLabel.setObjectName("usernameLabel")
        self.usernameEdit = QtWidgets.QLineEdit(JD)
        self.usernameEdit.setGeometry(QtCore.QRect(120, 120, 131, 21))
        self.usernameEdit.setObjectName("usernameEdit")
        self.usericonLabel2 = QtWidgets.QLabel(JD)
        self.usericonLabel2.setGeometry(QtCore.QRect(150, 30, 72, 71))
        self.usericonLabel2.setText("")
        self.usericonLabel2.setObjectName("usericonLabel2")
        self.usericonLabel = QtWidgets.QLabel(JD)
        self.usericonLabel.setGeometry(QtCore.QRect(50, 60, 72, 15))
        self.usericonLabel.setObjectName("usericonLabel")
        self.checklogbtn = QtWidgets.QPushButton(JD)
        self.checklogbtn.setGeometry(QtCore.QRect(50, 220, 201, 28))
        self.checklogbtn.setObjectName("checklogbtn")

        self.retranslateUi(JD)
        QtCore.QMetaObject.connectSlotsByName(JD)

    def retranslateUi(self, JD):
        _translate = QtCore.QCoreApplication.translate
        JD.setWindowTitle(_translate("JD", "京东模拟登陆"))
        self.timeLabel.setText(_translate("JD", "TextLabel"))
        self.LoginBtn.setText(_translate("JD", "扫码登录"))
        self.usernameLabel.setText(_translate("JD", "用户名："))
        self.usericonLabel.setText(_translate("JD", "头像："))
        self.checklogbtn.setText(_translate("JD", "我已扫码，检查是否登陆"))
