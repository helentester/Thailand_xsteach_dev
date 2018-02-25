# coding:utf-8
__author__ = 'Helen'
'''
description:共用模块，如登录功能
'''
from src.backendPages import Blogin_page,BsiteMenu_page
from selenium import webdriver


class public_module():
    # 后台登录功能
    def Blogin(self):
        self.driver = self.setUp_firefox()
        self.Blogin_page = Blogin_page.Blogin_page(self.driver)
        self.Blogin_page.open()
        self.Blogin_page.input_account('admin@xsteach.com')
        self.Blogin_page.input_password('xsteach')
        self.Blogin_page.input_captcha('xsteach')
        self.Blogin_page.click_loginButton()
        self.BsiteMenu_page = BsiteMenu_page.BsiteMenu_page(self.driver)
        self.BsiteMenu_page.click_language_zhCN()
        return self.driver

    # 加载firefox浏览器
    def setUp_firefox(self):
        profile_directory = r'C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\vlq8tn8d.default'
        profile = webdriver.FirefoxProfile(profile_directory)
        self.driver = webdriver.Firefox(profile)
        #self.driver = webdriver.Firefox()
        return self.driver