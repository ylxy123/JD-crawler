# @Time : 2020/2/29 15:06
# @Author : YLXY
# @File : main.py
# -*- coding: utf-8 -*-

import re
from time import sleep
import time
import threading
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver import Firefox
from selenium.webdriver import FirefoxOptions
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui as pag
import logging
import json
from PIL import Image
from show_img import show_qrimg
from mainWin import Ui_JD
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QLineEdit, QMessageBox, QDialog
import sys
import os
import datetime
from PyQt5 import Qt, QtGui
from PyQt5.QtCore import QDateTime, QTimer
from PyQt5 import QtCore
from PyQt5.Qt import QThread
from scanQR import Ui_Dialog

log_url = 'https://passport.jd.com/uc/login'
cur_url = ''


def headless_chrome(url):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get(url)
    return driver

def headless_firefox(url):
    profile = FirefoxOptions()
    profile.add_argument('-headless')
    driver = webdriver.Firefox(firefox_options=profile)
    driver.get(url)
    return driver

def log_init():
    logger = logging.getLogger('log.conf')
    logging.basicConfig(level=logging.DEBUG,
                        format="%(asctime)s %(name)s %(levelname)s %(message)s",
                        datefmt='%Y-%m-%d  %H:%M:%S %a', # 注意月份和天数不要搞乱了，这里的格式化符与time模块相同
                        filename='local.log'
                        )
    return logger



class EmittingStr(QtCore.QObject):
    textWritten = QtCore.pyqtSignal(str)  # 定义一个发送str的信号

    def write(self, text):
        self.textWritten.emit(str(text))


# 界面类
class JD_ui(QWidget,Ui_JD):
    def __init__(self):
        self.username = ''
        super(QWidget, self).__init__()
        self.setupUi(self)
        sys.stdout = EmittingStr(textWritten=self.outputWritten)
        sys.stderr = EmittingStr(textWritten=self.outputWritten)
        self.connecter()
        # 日志模块初始化
        self.logger = log_init()


        # 显示时间
        timer = QTimer(self)
        timer.timeout.connect(self.showtime)
        timer.start()

    def showtime(self):
        datetime = QDateTime.currentDateTime()
        timetext = datetime.toString()
        self.timeLabel.setText(timetext)


    def connecter(self):
        self.LoginBtn.clicked.connect(self.QRlogin)
        self.checklogbtn.clicked.connect(self.checklog)
        self.showQRbtn.clicked.connect(self.showQRcode)
        self.f5btn.clicked.connect(self.getInfo)

    def showQRcode(self):
        os.system('start ./qr/show.png')

    def QRlogin(self):
        # 接管已打开浏览器
        # chrome_options = Options()
        # chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        # chrome_driver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
        # driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)

        self.outputWritten('FireFox内核运行中...')

        # 无头浏览器模式
        self.driver = headless_firefox('https://passport.jd.com/uc/login')
        self.outputWritten('京东-欢迎登录')
        log_url = self.driver.current_url
        img = self.driver.find_element_by_class_name('qrcode-img')
        self.outputWritten('二维码跳转中...')

        # 保存二维码
        path = './qr/show.png'
        img.screenshot(path)
        QRcode = Image.open(path)
        QRcode.save(path)

        # 打开保存的二维码
        os.system('start ./qr/show.png')
        self.outputWritten("请扫码登录！！！")

    # 获取用户信息
    def getInfo(self):
        self.username = self.driver.find_element_by_class_name('nickname').text
        self.usernameEdit.setText(self.username)
        self.driver.get('https://i.jd.com/user/userinfo/showImg.html')
        self.outputWritten(self.driver.title)
        try:
            img = self.driver.find_element_by_class_name('img-s')
            img.screenshot('./qr/icon.png')
            Icon = Image.open('./qr/icon.png')
            Icon.save('./qr/icon.png')
        except BaseException as e:
            self.outputWritten('未知错误')
            self.outputWritten(f'{e}')
        else:
            self.usericonLabel2.setStyleSheet("image: url(:/头像/qr/icon.png);")


    # 检测是否登录
    def checklog(self):
        try:
            cur_url = self.driver.current_url
            if cur_url == log_url:
                self.outputWritten('请注意：二维码未扫描！请扫二维码登录')
            else:
                self.outputWritten('登录成功！！！')

        except BaseException:
            self.outputWritten('未检测到登录信息，请重试！！！')
        else:
            # 保存登录cookies
            cookies = self.driver.get_cookies()
            jsonCookies = json.dumps(cookies)

            # 存于本地
            with open('cookies.json', 'w') as f:
                f.write(jsonCookies)






    def getlocalcookies(self):
        pass







    def outputWritten(self, text):
        self.logger.info(text)
        cursor = self.log_terminal.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(f'>>> {datetime.datetime.now()} ' + '- ' + text + '\n')
        self.log_terminal.setTextCursor(cursor)
        self.log_terminal.ensureCursorVisible()







if __name__ == '__main__':

    app = QApplication(sys.argv)
    jd = JD_ui()
    jd.show()
    sys.exit(app.exec())






