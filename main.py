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
from PIL import Image
from show_img import show_qrimg

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

if __name__ == '__main__':
    logger = log_init()

    # 接管已打开浏览器
    # chrome_options = Options()
    # chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    # chrome_driver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
    # driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
    logger.info('FireFox内核运行中...')
    # 无头浏览器模式
    driver = headless_firefox('https://www.jd.com/')


    # driver = webdriver.Chrome()
    # driver.get('https://www.jd.com/')

    if driver.title == "京东(JD.COM)-正品低价、品质保障、配送及时、轻松购物！":
        logger.info('京东(JD.COM)-正品低价、品质保障、配送及时、轻松购物！')
        driver.find_element_by_class_name('link-login').click()
        # WebDriverWait(driver,10)
    logger.info('京东-欢迎登录')
    img = driver.find_element_by_class_name('qrcode-login')
    logger.info('二维码跳转中...')
    # 执行鼠标动作
    # actions = ActionChains(driver)
    # actions.context_click(img)
    # actions.perform()
    # pag.typewrite(['down','down','enter','enter'])
    # sleep(1)
    # pag.typewrite(['enter'])

    # 打开二维码
    # 保存二维码
    path = './qr/show.png'
    img.screenshot(path)
    QRcode = Image.open(path)
    QRcode.save(path)


    # 打开保存的二维码
    show_qrimg('./qr/show.png')
    logger.info('请扫描二维码')





