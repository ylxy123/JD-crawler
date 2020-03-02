# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scanQR.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(189, 220)
        Dialog.setMinimumSize(QtCore.QSize(189, 220))
        Dialog.setMaximumSize(QtCore.QSize(189, 220))
        self.QRLabel = QtWidgets.QLabel(Dialog)
        self.QRLabel.setGeometry(QtCore.QRect(0, 0, 191, 181))
        self.QRLabel.setStyleSheet("image: url(:/QRcode/qr/show.png);")
        self.QRLabel.setText("")
        self.QRLabel.setObjectName("QRLabel")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(-10, 0, 20, 221))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(180, 0, 20, 221))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(0, -10, 191, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(Dialog)
        self.line_4.setGeometry(QtCore.QRect(0, 210, 191, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.scanBtn = QtWidgets.QPushButton(Dialog)
        self.scanBtn.setGeometry(QtCore.QRect(20, 180, 151, 31))
        self.scanBtn.setObjectName("scanBtn")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "请扫二维码"))
        self.scanBtn.setText(_translate("Dialog", "检测是否登录"))
import QR_rc
