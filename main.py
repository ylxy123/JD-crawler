# @Time : 2020/2/29 15:06
# @Author : YLXY
# @File : main.py
# -*- coding: utf-8 -*-

import re
from time import sleep
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
from PyQt5 import Qt
from PyQt5.QtCore import QDateTime, QTimer
from PyQt5 import QtCore
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
    logger.setLevel(logging.DEBUG)

    # 终端记录handler
    hterm = logging.StreamHandler()
    hterm.setLevel(logging.INFO)

    # 文件记录handler
    hfile = logging.FileHandler('local.log')
    hfile.setLevel(logging.DEBUG)

    # 日志格式
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    hterm.setFormatter(formatter)
    hfile.setFormatter(formatter)

    logger.addHandler(hterm)
    logger.addHandler(hfile)

    DATE_FORMAT = '%Y-%m-%d  %H:%M:%S '  # 配置输出时间的格式，注意月份和天数不要搞乱了
    return logger







# 界面类
class JD_ui(QWidget,Ui_JD):
    def __init__(self):
        super(QWidget, self).__init__()
        self.setupUi(self)
        self.connecter()

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
        

    def QRlogin(self):
        # 日志模块初始化
        logger = log_init()

        # 接管已打开浏览器
        # chrome_options = Options()
        # chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        # chrome_driver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
        # driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)

        logger.info('FireFox内核运行中...')

        # 无头浏览器模式
        driver = headless_firefox(self.log_url)
        logger.info('京东-欢迎登录')
        self.log_url = driver.current_url
        img = driver.find_element_by_class_name('qrcode-img')
        logger.info('二维码跳转中...')

        # 保存二维码
        path = './qr/show.png'
        img.screenshot(path)
        QRcode = Image.open(path)
        QRcode.save(path)

        # 打开保存的二维码

        logger.info('请扫描二维码')
        self.cur_url = driver.current_url
        while self.cur_url == self.log_url:
            logger.warn('请注意：二维码未扫描！请扫二维码登录')
            self.cur_url = driver.current_url
        logger.info('登录成功！！！')

        # 保存登录cookies
        cookies = driver.get_cookies()
        jsonCookies = json.dumps(cookies)

        # 存于本地
        with open('cookies.json', 'w') as f:
            f.write(jsonCookies)
        driver.quit()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    jd = JD_ui()
    jd.show()
    sys.exit(app.exec())






