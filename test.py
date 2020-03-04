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

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)

print(driver.title)

# 保存主页面句柄
mainWin = driver.current_window_handle

driver.get('https://i.jd.com/user/userinfo/showImg.html')


username = driver.find_element_by_class_name('nickname').text
img = driver.find_elements_by_css_selector("bigImage")
imgpath = './qr/icon.png'
print(type(img))
img.screenshot(imgpath)
# Icon = Image.open(imgpath)
# Icon.save(imgpath)
# os.system('start ' + imgpath)



print(username)




