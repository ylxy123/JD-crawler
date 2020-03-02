# @Time : 2020/3/1 21:31
# @Author : YLXY
# @File : test1.py
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
import sys
from MyMainDialog import Ui_Dialog
from mySubDialog import Ui_Dialog2

class SubDialog(QDialog,Ui_Dialog2):
    def __init__(self):
        super(SubDialog,self).__init__()
        self.setupUi2(self)
        self.setWindowTitle("自定义消息对话框：登录窗口")

class MainDialog(QDialog,Ui_Dialog):
    def __init__(self):
        super(MessageDialog,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("消息对话框实验")
        self.pushButton.clicked.connect(self.slotcalldialog)
    def slotcalldialog(self): #调用其他自定义消息框
        self.newDialog=SubDialog()
        self.newDialog.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainDialog()
    main.show()
    sys.exit(app.exec_())
