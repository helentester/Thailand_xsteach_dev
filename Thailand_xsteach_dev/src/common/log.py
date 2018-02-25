# coding:utf-8
__author__ = 'Helen'
'''
description:配置日志文件，输出INFO级别以上的日志
'''

import logging
from config import globalparameter as gl


class log:
    def __init__(self):
        self.logname = "mylog"

    def setMSG(self, level, msg):
        # 之前把下面定义log的一大段代码写在了__init__里面，造成了日志重复输出
        # 此大坑，谨记谨记！！！!
        logger = logging.getLogger()
        # 定义Handler输出到文件和控制台
        fh = logging.FileHandler(gl.log_path)
        ch = logging.StreamHandler()
        # 定义日志输出格式
        formater = logging.Formatter("%(asctime)s %(levelname)s %(message)s' ")
        fh.setFormatter(formater)
        ch.setFormatter(formater)
        # 添加Handler
        logger.addHandler(fh)
        logger.addHandler(ch)
        # 添加日志信息，输出INFO级别的信息
        logger.setLevel(logging.INFO)
        if level=='debug':
            logger.debug(msg)
        elif level=='info':
            logger.info(msg)
        elif level=='warning':
            logger.warning(msg)
        elif level=='error':
            logger.error(msg)
        # 移除句柄，否则日志会重复输出
        logger.removeHandler(fh)
        logger.removeHandler(ch)
        fh.close()

    def debug(self, msg):
        self.setMSG('debug', msg)

    def info(self, msg):
        self.setMSG('info', msg)

    def warning(self, msg):
        self.setMSG('warning', msg)

    def error(self, msg):
        self.setMSG('error', msg)
