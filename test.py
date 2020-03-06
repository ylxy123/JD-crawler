# @Time : 2020/3/1 9:24
# @Author : YLXY
# @File : test.py
# -*- coding: utf-8 -*-


# USER-AGENT Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36


from selenium import webdriver
import requests
import json
import pickle
import time
import os
import re
from PIL import Image
from selenium.webdriver import Firefox
from selenium.webdriver import FirefoxOptions
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions

from selenium.webdriver.chrome.options import Options


def isElemExist(driver, elem):
    flag = True
    try:
        driver.find_element_by_class_name(elem)
        return flag
    except BaseException:
        flag = False
        return flag



if __name__ == '__main__':
    # chrome_options = Options()
    # chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    # chrome_driver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
    # driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
    #
    # print(driver.title)
    #
    # # 保存主页面句柄
    # mainWin = driver.current_window_handle
    # driver.get('https://cart.jd.com/cart.action')
    #
    # print(driver.title)
    #
    # if isElemExist(driver, 'number'):
    #     print('存在')
    #     print(driver.find_element_by_class_name('number').text)
    # else:
    #     print('不存在')

    print(os.path.isfile('cookies.txt'))








