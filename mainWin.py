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
        JD.resize(791, 586)
        JD.setMinimumSize(QtCore.QSize(791, 586))
        font = QtGui.QFont()
        font.setFamily("黑体")
        JD.setFont(font)
        JD.setStyleSheet("")
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
        self.log_terminal.setGeometry(QtCore.QRect(40, 371, 711, 151))
        self.log_terminal.setStyleSheet("background-color: rgb(60, 63, 65);\n"
"color: rgb(255, 255, 255);")
        self.log_terminal.setObjectName("log_terminal")
        self.LoginBtn = QtWidgets.QPushButton(JD)
        self.LoginBtn.setGeometry(QtCore.QRect(50, 150, 91, 28))
        self.LoginBtn.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.LoginBtn.setObjectName("LoginBtn")
        self.usernameLabel = QtWidgets.QLabel(JD)
        self.usernameLabel.setGeometry(QtCore.QRect(50, 110, 101, 21))
        self.usernameLabel.setObjectName("usernameLabel")
        self.usernameEdit = QtWidgets.QLineEdit(JD)
        self.usernameEdit.setGeometry(QtCore.QRect(120, 110, 131, 21))
        self.usernameEdit.setStyleSheet("background-color: rgb(222, 222, 222);")
        self.usernameEdit.setObjectName("usernameEdit")
        self.usericonLabel2 = QtWidgets.QLabel(JD)
        self.usericonLabel2.setGeometry(QtCore.QRect(130, 40, 61, 61))
        self.usericonLabel2.setStyleSheet("image: url(:/头像/qr/头像.png);")
        self.usericonLabel2.setText("")
        self.usericonLabel2.setObjectName("usericonLabel2")
        self.usericonLabel = QtWidgets.QLabel(JD)
        self.usericonLabel.setGeometry(QtCore.QRect(50, 70, 72, 15))
        self.usericonLabel.setObjectName("usericonLabel")
        self.checklogbtn = QtWidgets.QPushButton(JD)
        self.checklogbtn.setGeometry(QtCore.QRect(50, 220, 201, 28))
        self.checklogbtn.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.checklogbtn.setObjectName("checklogbtn")
        self.line_5 = QtWidgets.QFrame(JD)
        self.line_5.setGeometry(QtCore.QRect(20, 260, 751, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.showQRbtn = QtWidgets.QPushButton(JD)
        self.showQRbtn.setGeometry(QtCore.QRect(160, 150, 91, 28))
        self.showQRbtn.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.showQRbtn.setObjectName("showQRbtn")
        self.line_6 = QtWidgets.QFrame(JD)
        self.line_6.setGeometry(QtCore.QRect(270, 20, 20, 261))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(JD)
        self.line_7.setGeometry(QtCore.QRect(20, 270, 751, 20))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(JD)
        self.line_8.setGeometry(QtCore.QRect(20, 20, 751, 20))
        self.line_8.setStyleSheet("color: rgb(170, 255, 255);")
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_10 = QtWidgets.QFrame(JD)
        self.line_10.setGeometry(QtCore.QRect(20, 20, 20, 531))
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.line_11 = QtWidgets.QFrame(JD)
        self.line_11.setGeometry(QtCore.QRect(20, 340, 751, 20))
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.label = QtWidgets.QLabel(JD)
        self.label.setGeometry(QtCore.QRect(40, 350, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe Caslon Pro Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.line_12 = QtWidgets.QFrame(JD)
        self.line_12.setGeometry(QtCore.QRect(130, 30, 61, 20))
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.line_13 = QtWidgets.QFrame(JD)
        self.line_13.setGeometry(QtCore.QRect(130, 90, 61, 20))
        self.line_13.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.line_14 = QtWidgets.QFrame(JD)
        self.line_14.setGeometry(QtCore.QRect(120, 40, 20, 61))
        self.line_14.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.line_15 = QtWidgets.QFrame(JD)
        self.line_15.setGeometry(QtCore.QRect(180, 40, 20, 61))
        self.line_15.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_15.setObjectName("line_15")
        self.line_16 = QtWidgets.QFrame(JD)
        self.line_16.setGeometry(QtCore.QRect(750, 20, 20, 531))
        self.line_16.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_16.setObjectName("line_16")
        self.line_17 = QtWidgets.QFrame(JD)
        self.line_17.setGeometry(QtCore.QRect(20, 530, 751, 20))
        self.line_17.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_17.setObjectName("line_17")
        self.f5btn = QtWidgets.QPushButton(JD)
        self.f5btn.setGeometry(QtCore.QRect(200, 60, 51, 28))
        self.f5btn.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.f5btn.setObjectName("f5btn")
        self.goodsEdit = QtWidgets.QLineEdit(JD)
        self.goodsEdit.setGeometry(QtCore.QRect(450, 60, 291, 21))
        self.goodsEdit.setStyleSheet("background-color: rgb(211, 211, 211);")
        self.goodsEdit.setObjectName("goodsEdit")
        self.label_3 = QtWidgets.QLabel(JD)
        self.label_3.setGeometry(QtCore.QRect(300, 60, 131, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(JD)
        self.label_4.setGeometry(QtCore.QRect(290, 30, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.line_9 = QtWidgets.QFrame(JD)
        self.line_9.setGeometry(QtCore.QRect(280, 140, 481, 16))
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.relogbtn = QtWidgets.QPushButton(JD)
        self.relogbtn.setGeometry(QtCore.QRect(50, 190, 201, 21))
        self.relogbtn.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.relogbtn.setObjectName("relogbtn")
        self.widget = QtWidgets.QWidget(JD)
        self.widget.setGeometry(QtCore.QRect(300, 100, 441, 31))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.cartnumberEdit = QtWidgets.QLineEdit(self.widget)
        self.cartnumberEdit.setStyleSheet("background-color: rgb(222, 222, 222);")
        self.cartnumberEdit.setObjectName("cartnumberEdit")
        self.horizontalLayout.addWidget(self.cartnumberEdit)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.addcartbtn = QtWidgets.QPushButton(self.widget)
        self.addcartbtn.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.addcartbtn.setObjectName("addcartbtn")
        self.horizontalLayout.addWidget(self.addcartbtn)
        self.timeLabel.raise_()
        self.line_4.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.line_3.raise_()
        self.log_terminal.raise_()
        self.LoginBtn.raise_()
        self.usernameLabel.raise_()
        self.usernameEdit.raise_()
        self.usericonLabel2.raise_()
        self.usericonLabel.raise_()
        self.checklogbtn.raise_()
        self.line_5.raise_()
        self.showQRbtn.raise_()
        self.line_6.raise_()
        self.line_7.raise_()
        self.line_8.raise_()
        self.line_10.raise_()
        self.line_11.raise_()
        self.label.raise_()
        self.line_12.raise_()
        self.line_14.raise_()
        self.line_15.raise_()
        self.line_16.raise_()
        self.line_17.raise_()
        self.f5btn.raise_()
        self.line_13.raise_()
        self.label_2.raise_()
        self.cartnumberEdit.raise_()
        self.goodsEdit.raise_()
        self.label_3.raise_()
        self.addcartbtn.raise_()
        self.label_4.raise_()
        self.line_9.raise_()
        self.relogbtn.raise_()

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
        self.showQRbtn.setText(_translate("JD", "显示二维码"))
        self.label.setText(_translate("JD", "terminal"))
        self.f5btn.setText(_translate("JD", "刷新"))
        self.label_3.setText(_translate("JD", "待添加的商品码："))
        self.label_4.setText(_translate("JD", "购物车"))
        self.relogbtn.setText(_translate("JD", "恢复历史登录"))
        self.label_2.setText(_translate("JD", "当前购物车数量："))
        self.addcartbtn.setText(_translate("JD", "添加并查询购物车数量"))
import QR_rc
