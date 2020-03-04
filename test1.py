# @Time : 2020/3/1 21:31
# @Author : YLXY
# @File : test1.py
# -*- coding: utf-8 -*-

import requests
import json
import time
import re
import pickle
import os
import random

class JD(object):
    def __init__(self):
        self.sess = requests.Session()
        self.sess.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "Referer": "https://order.jd.com/center/list.action",
            "Connection": "keep-alive"
        }

        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/531.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "Referer": "https://cart.jd.com/cart.action",
            "Connection": "keep-alive"
        }

        self.speed = 5000
        # self.isLogin = False
        self.cookiesString = ''
        self.cookies = {}
        self.skuidString = ''
        self.skuid = []
        self.cont = 1



# login
    def loginByQR(self):
        # jd login by QR code
        try:
            self.updateStateText('请您打开京东手机客户端或微信扫一扫, 准备扫码登录')

            urls = (
                'https://passport.jd.com/new/login.aspx',
                'https://qr.m.jd.com/show',
                'https://qr.m.jd.com/check',
                'https://passport.jd.com/uc/qrCodeTicketValidation'
            )
            # step 1: open login page
            response = self.sess.get(
                urls[0],
                headers=self.headers
            )
            if response.status_code != requests.codes.OK:
                self.updateStateText(f'获取登录页失败: {response.status_code}')
                # self.isLogin = False
                return False
            # update cookies
            self.cookies.update(response.cookies)
            self.sess.cookies = response.cookies

            # step 2: get QR image
            response = self.sess.get(
                urls[1],
                headers=self.headers,
                cookies=self.cookies,
                params={
                    'appid': 133,
                    'size': 147,
                    't': int(time.time() * 1000),
                }
            )
            if response.status_code != requests.codes.OK:
                self.updateStateText(f'获取二维码失败: {response.status_code}')
                # self.isLogin = False
                return False

            # update cookies
            self.cookies.update(response.cookies)
            self.sess.cookies = response.cookies

            # save QR code
            image_file = 'qr.png'
            with open(image_file, 'wb') as f:
                for chunk in response.iter_content(chunk_size=1024):
                    f.write(chunk)

            # scan QR code with phone
            if os.name == "nt":
                # for windows
                os.system('start ' + image_file)
            else:
                if os.uname()[0] == "Linux":
                    # for linux platform
                    os.system("eog " + image_file)
                else:
                    # for Mac platform
                    os.system("open " + image_file)

            # step 3: check scan result
            self.headers['Host'] = 'qr.m.jd.com'
            self.headers['Referer'] = 'https://passport.jd.com/new/login.aspx'

            # check if QR code scanned
            qr_ticket = None
            retry_times = 1000  # 尝试1000次
            while retry_times:
                retry_times -= 1
                response = self.sess.get(
                    urls[2],
                    headers=self.headers,
                    cookies=self.cookies,
                    params={
                        'callback': 'jQuery%d' % random.randint(1000000, 9999999),
                        'appid': 133,
                        'token': self.cookies['wlfstk_smdl'],
                        '_': int(time.time() * 1000)
                    }
                )
                if response.status_code != requests.codes.OK:
                    continue
                rs = json.loads(re.search(r'{.*?}', response.text, re.S).group())
                if rs['code'] == 200:
                    self.updateStateText(f"{rs['ticket']}(Response Code: {rs['code']})")
                    qr_ticket = rs['ticket']
                    break
                else:
                    self.updateStateText(f"{rs['msg']}(Response Code: {rs['code']})")
                    time.sleep(2)

            if not qr_ticket:
                self.updateStateText("ERROR: 二维码登录失败")
                # self.isLogin = False
                return False

            # step 4: validate scan result
            self.headers['Host'] = 'passport.jd.com'
            self.headers['Referer'] = 'https://passport.jd.com/new/login.aspx'
            response = requests.get(
                urls[3],
                headers=self.headers,
                cookies=self.cookies,
                params={'t': qr_ticket},
            )
            if response.status_code != requests.codes.OK:
                self.updateStateText(f"二维码登录校验失败: {response.status_code}")
                # self.isLogin = False
                return False

            # 京东有时会认为当前登录有危险, 需要手动验证
            # url: https://safe.jd.com/dangerousVerify/index.action?username=...
            res = json.loads(response.text)
            if not response.headers.get('p3p'):
                if 'url' in res:
                    self.updateStateText(f"请进行手动安全验证: {res['url']}")
                    # self.isLogin = False
                    return False
                else:
                    self.updateStateText('登录失败, ERROR: ' + res)
                    # self.isLogin = False
                    return False

            # login succeed
            self.headers['P3P'] = response.headers.get('P3P')
            self.cookies.update(response.cookies)
            self.sess.cookies = response.cookies

            # save cookie
            with open('cookie', 'w+') as f:
                f.write(json.dumps(self.cookies))

            self.updateStateText("登录成功!")
            # self.isLogin = True
            self.getUsername()
            return True

        except Exception as e:
            # self.isLogin = False
            self.updateStateText('ERROR: ' + str(e))
            raise


    def getUsername(self):
        userName_Url = 'https://passport.jd.com/new/helloService.ashx?callback=jQuery339448&_=' + str(
            int(time.time() * 1000))

        resp = self.sess.get(url=userName_Url, allow_redirects=True)
        resultText = resp.text
        resultText = resultText.replace('jQuery339448(', '')
        resultText = resultText.replace(')', '')
        usernameJson = json.loads(resultText)
        self.updateStateText('账号名称: ' + usernameJson['nick'])

    def updateStateText(self, stateText):
        print(stateText)

    def checkLogin(self):
        self.updateStateText('验证登录状态...')
        for flag in range(1, 3):
            try:
                targetURL = 'https://order.jd.com/center/list.action'
                payload = {
                    'rid': str(int(time.time() * 1000)),
                }
                resp = self.sess.get(url=targetURL, params=payload, allow_redirects=False)
                if resp.status_code == requests.codes.OK:
                    self.updateStateText('登录成功!')
                    return True
                else:
                    self.updateStateText('第 %s 次再尝试验证cookie...' % flag)
                    self.updateStateText('正在尝试从历史讯息中恢复...')
                    with open('cookie', 'rb') as f:
                        cookies = requests.utils.cookiejar_from_dict(pickle.load(f))
                    # print(cookies)
                    self.sess.cookies = cookies
                    continue
            except Exception as e:
                self.updateStateText(str(e))
                self.updateStateText('第 %s 次再尝试验证cookie...' % flag)
                continue
        self.updateStateText('请登录!')
        return False

if __name__ == '__main__':
    jd = JD()
    jd.loginByQR()
    jd.checkLogin()
