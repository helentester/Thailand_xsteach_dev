# coding:utf-8
__author__ = 'Helen'
'''
description:后台登录页面
'''
from src.common.Base_Page import BasePage
from selenium.webdriver.common.by import By
from config import globalparameter as gl


class Blogin_page(BasePage):
    # 定位器
    account_loc = (By.CSS_SELECTOR, '#loginform-account')
    password_loc = (By.CSS_SELECTOR, '#loginform-password')
    captcha_loc = (By.CSS_SELECTOR, '#loginform-captcha')
    loginButton_loc = (By.CSS_SELECTOR, '.btn.btn-primary')

    # 打开登录页面
    def open(self):
        self._open(gl.backend_URL,u'XSTEACH')

    # 输入账号
    def input_account(self,account):
        self.send_keys(account, *self.account_loc)

    # 输入密码
    def input_password(self,password):
        self.send_keys(password, *self.password_loc)

    # 输入验证码
    def input_captcha(self,captcha):
        self.send_keys(captcha, *self.captcha_loc)

    # 点击登录按钮
    def click_loginButton(self):
        self.find_element(*self.loginButton_loc).click()
