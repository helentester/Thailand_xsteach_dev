# coding:utf-8
__author__ = 'Helen'
'''
description:编辑学员页面
'''
from selenium.webdriver.common.by import By
from src.common.Base_Page import BasePage


class BstudentEdit_page(BasePage):
    # 定位器
    studentName_loc = (By.CSS_SELECTOR, '#users-username')
    password_loc = (By.CSS_SELECTOR, '#users-password')
    email_loc = (By.CSS_SELECTOR, '#users-email')
    submit_button_loc = (By.CSS_SELECTOR, '.btn.btn-primary.offset')

    # 输入学员昵称
    def input_studentName(self, studentName):
        self.send_keys(studentName,*self.studentName_loc)

    # 输入密码
    def input_password(self, password):
        self.send_keys(password,*self.password_loc)

    # 输入邮箱
    def input_email(self, email):
        self.send_keys(email,*self.email_loc)

    # 点击提交按钮
    def click_submit_button(self):
        self.find_element(*self.submit_button_loc).click()
