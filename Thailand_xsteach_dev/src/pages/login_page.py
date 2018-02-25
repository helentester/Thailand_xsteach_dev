# coding:utf-8
__author__ = 'Helen'
'''
description:泰国官网登录页面
'''
from src.common.Base_Page import BasePage
from selenium.webdriver.common.by import By


class login_page(BasePage):
    # 定位器
    username_loc = (By.ID,'loginform-account')
    password_loc = (By.ID,'loginform-password')
    login_button_log = (By.NAME,'login-button')

    # 输入用户名
    def input_username(self,username):
        self.send_keys(username,*self.username_loc)

    # 输入密码
    def input_password(self,password):
        self.send_keys(password,*self.password_loc)

    # 点击登录按钮
    def click_login_button(self):
        self.find_element(*self.login_button_log).click()

