# coding:utf-8
__author__ = 'Helen'
'''
description:编辑用户页面
'''
from src.common.Base_Page import BasePage
from selenium.webdriver.common.by import By


class BuserEdit_page(BasePage):
    # 定位器
    mobile_loc = (By.CSS_SELECTOR, "#adminform-mobile")
    password_loc = (By.CSS_SELECTOR, "#adminform-password")
    name_loc = (By.CSS_SELECTOR, "#adminform-name")
    email_loc = (By.CSS_SELECTOR, "#adminform-email")
    department_loc = (By.CSS_SELECTOR, "#adminform-department_id>option[value='12']")
    submit_button_loc = (By.CSS_SELECTOR, ".btn.btn-primary.offset")

    # 输入电话
    def input_mobile(self, mobile):
        self.send_keys(mobile, *self.mobile_loc)

    # 输入密码
    def input_password(self, password):
        self.send_keys(password, *self.password_loc)

    # 输入真实姓名
    def input_name(self, userName):
        self.send_keys(userName, *self.name_loc)

    # 输入邮箱
    def input_email(self, email):
        self.send_keys(email, *self.email_loc)

    # 选择部门
    def click_department(self):
        self.find_element(*self.department_loc).click()

    # 点击提交按钮
    def click_submit_button(self):
        self.find_element(*self.submit_button_loc).click()
