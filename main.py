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
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
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
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QDateTime, QTimer
from PyQt5 import QtCore
# from PyQt5.Qt import QThread


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
                        datefmt='%Y-%m-%d  %H:%M:%S %a', # 这里的格式化符与time模块相同
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
        self.logflag = False
        self.cookies = ''
        super(QWidget, self).__init__()
        self.setupUi(self)
        sys.stdout = EmittingStr(textWritten=self.outputWritten)
        sys.stderr = EmittingStr(textWritten=self.outputWritten)
        self.connecter()
        # 日志模块初始化
        self.logger = log_init()
        self.dataInit()


        # 显示时间
        timer = QTimer(self)
        timer.timeout.connect(self.showtime)
        timer.start()

    def showtime(self):
        datetime = QDateTime.currentDateTime()
        timetext = datetime.toString()
        self.timeLabel.setText(timetext)

    def dataInit(self):
        self.buynumBox.setMinimum(1)
        self.buynumBox.setMaximum(5)
        self.goodsEdit.setText('  11~12位纯数字')


    def connecter(self):
        self.LoginBtn.clicked.connect(self.QRlogin)
        self.checklogbtn.clicked.connect(self.checklog)
        self.showQRbtn.clicked.connect(self.showQRcode)
        self.f5btn.clicked.connect(self.getInfo)
        self.additembtn.clicked.connect(self.addtocart)
        self.searchCartbtn.clicked.connect(self.getcartInfo)
        self.relogbtn.clicked.connect(self.relogin)

    def showQRcode(self):
        os.system('start ./qr/show.png')

    def QRlogin(self):
        # 接管已打开浏览器
        # chrome_options = Options()
        # chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        # chrome_driver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
        # driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)

        self.outputWritten('FireFox内核运行中...')
        QApplication.processEvents()
        # 无头浏览器模式
        try:
            self.driver = headless_firefox('https://passport.jd.com/uc/login')
        except BaseException:
            self.outputWritten('连接超时，请检查网络连接')
        else:
            self.outputWritten('京东-欢迎登录')
            QApplication.processEvents()
            log_url = self.driver.current_url
            img = self.driver.find_element_by_class_name('qrcode-img')
            self.outputWritten('二维码跳转中...')
            QApplication.processEvents()
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
        self.outputWritten('正在获取用户信息...')
        QApplication.processEvents()
        try:
            self.username = self.driver.find_element_by_class_name('nickname').text
            self.usernameEdit.setText(self.username)
            self.driver.get('https://i.jd.com/user/userinfo/showImg.html')
        except BaseException :
            self.outputWritten("获取登录信息失败，请重新登录")
        else:
            try:
                if not os.path.exists('./qr/icon.png'):
                    img = self.driver.find_element_by_class_name('img-s')
                    img.screenshot('./qr/icon.png')
                    Icon = Image.open('./qr/icon.png')
                    Icon.save('./qr/icon.png')
            except BaseException as e:
                self.outputWritten('未知错误:'+f'{e}')
            else:
                self.usericonLabel2.setStyleSheet("image: url(:/头像/qr/icon.png);")
                QApplication.processEvents()


    # 获取购物车信息
    def getcartInfo(self):
        try:
            self.driver.get('https://cart.jd.com/cart.action')
        except BaseException:
            self.outputWritten('请求购物车信息失败！请检查是否登录')
        else:
            if self.isElemExist('cart-empty'):
                self.cartnumberEdit.setText('0')
                self.outputWritten('购物车为空！')
                return
            try:
                cartnum = self.driver.find_element_by_class_name('number').text
                self.driver.implicitly_wait(10)
            except BaseException as e:
                self.outputWritten(f'{e}')
            else:
                self.outputWritten('获取购物车信息成功，当前购物车商品数量：%c'%cartnum)
                self.cartnumberEdit.setText(cartnum)


    # 检测是否登录
    def checklog(self):
        try:
            cur_url = self.driver.current_url
            if cur_url == log_url:
                self.outputWritten('请注意：二维码未扫描！请扫二维码登录')
            else:
                self.outputWritten('您已登录！')
        except BaseException:
            self.outputWritten('未检测到登录信息，请重新登录！')
        else:
            self.getInfo()
            self.logflag == True
            # 保存登录cookies
            self.cookies = self.driver.get_cookies()
            # 存于本地
            with open("cookies.txt", "w") as f:
                json.dump(self.cookies, f)

    # 从已保存的cookies中恢复登录
    def relogin(self):
        self.outputWritten('正在尝试恢复历史登录信息...')
        self.outputWritten('Please wait...')
        QApplication.processEvents()
        try:
            self.driver = headless_firefox('https://www.jd.com/')
        except BaseException:
            self.outputWritten('连接超时，请检查网络连接')
        else:
            with open('cookies.txt','r') as f:
                cookies = json.load(f)
                for cookie in cookies:
                    self.driver.add_cookie(cookie)
            self.driver.get('https://www.jd.com/')
            self.username = self.driver.find_element_by_class_name('nickname').text
            if self.username == 'ylxy123':
                self.outputWritten("登录成功！！！")

    # 检测元素是否存在
    def isElemExist(self, elem):
        flag = True
        try:
            self.driver.find_element_by_class_name(elem)
            return flag
        except BaseException:
            flag = False
            return flag



    # 将商品添加进购物车
    def addtocart(self):
        self.outputWritten('正在将商品添加至购物车，请稍后...')
        QApplication.processEvents()
        itemcode = self.goodsEdit.text()
        item_url = 'https://item.jd.com/' + itemcode + '.html'
        try:
            self.driver.get(item_url)
            if itemcode == '' or not re.match(r'\d{6,13}', itemcode):
                self.outputWritten('商品码为空或非纯数字，请填写正确的商品码！')
                return
            item_num = str(self.buynumBox.text())
            # self.driver.find_element_by_css_selector('input#buy-num').send_keys(item_num)
            addurl = self.driver.find_element_by_css_selector('a#InitCartUrl').get_attribute('href')
            m = re.match(r'(.*&pcount=)(\d{1,2})(.*)', addurl)
            a = m.group(1)
            c = m.group(3)
            addurl1 = a + item_num + c
            self.driver.get(addurl1)
        except BaseException :
            self.outputWritten('添加失败，请检查是否登录')
        else:
            self.outputWritten('添加购物车成功！！！')


    # GUI terminal
    def outputWritten(self, text):
        self.logger.info(text)
        cursor = self.log_terminal.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(f'>>> {datetime.datetime.now()} ' + '- ' + text + '\n')
        self.log_terminal.setTextCursor(cursor)
        self.log_terminal.ensureCursorVisible()



def jd_main():
    app = QApplication(sys.argv)
    jd = JD_ui()
    jd.show()
    sys.exit(app.exec())



if __name__ == '__main__':
    jd_main()







