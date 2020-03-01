# @Time : 2020/3/1 9:24
# @Author : YLXY
# @File : test.py
# -*- coding: utf-8 -*-

import logging

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
    formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(message)s')

    hterm.setFormatter(formatter)
    hfile.setFormatter(formatter)

    logger.addHandler(hterm)
    logger.addHandler(hfile)

    DATE_FORMAT = '%Y-%m-%d  %H:%M:%S '  # 配置输出时间的格式，注意月份和天数不要搞乱了
    return logger


logger = log_init()
logger.info("1111111")
# USER-AGENT Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36