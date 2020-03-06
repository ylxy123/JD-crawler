# @Time : 2020/3/6 16:52
# @Author : YLXY
# @File : 多线程.py
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

global sec
sec = 0


class WorkThread(QThread):
    #实例化一个信号对象
    trigger = pyqtSignal()

    def __int__(self):
        super(WorkThread, self).__init__()

    def run(self):
        #开始进行循环
        for i in range(2000000000):
            pass

        # 循环完毕后发出信号
        self.trigger.emit()


def countTime():
    global sec
    sec += 1
    # LED显示数字+1
    lcdNumber.display(sec)


def work():
    # 计时器每秒计数
    timer.start(1000)
    # 计时开始
    workThread.start()
    # 当获得循环完毕的信号时，停止计数
    workThread.trigger.connect(timeStop)


def timeStop():
    #定时器停止
    timer.stop()
    print("运行结束用时", lcdNumber.value())
    global sec
    sec = 0


if __name__ == "__main__":
    app = QApplication(sys.argv)
    top = QWidget()
    top.resize(300, 120)

    # 垂直布局类QVBoxLayout
    layout = QVBoxLayout(top)

    # 加显示屏，按钮到布局中
    lcdNumber = QLCDNumber()
    layout.addWidget(lcdNumber)
    button = QPushButton("测试")
    layout.addWidget(button)

    #实例化定时器与多线程类
    timer = QTimer()
    workThread = WorkThread()

    button.clicked.connect(work)
    # 每次计时结束，触发 countTime
    timer.timeout.connect(countTime)

    top.show()
    sys.exit(app.exec_())
