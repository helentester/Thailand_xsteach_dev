# coding:utf-8
__author__ = 'Helen'
'''
description:编辑广告组页面
'''
from selenium.webdriver.common.by import By
from src.common.Base_Page import BasePage


class BadGroupEdit_page(BasePage):
    # 定位器
    name_loc = (By.CSS_SELECTOR, "#adgroup-name")   # 广告组名称
    code_loc = (By.CSS_SELECTOR, "#adgroup-code")   # 标识符
    submit_button_loc = (By.CSS_SELECTOR, ".btn.btn-primary.offset")    # 提交按钮

    # 输入广告组名称
    def input_name(self, group_name):
        self.send_keys(group_name, *self.name_loc)

    # 输入标识符
    def input_code(self, group_code):
        self.send_keys(group_code, *self.code_loc)

    # 点击提交按钮
    def click_submit_button(self):
        self.find_element(*self.submit_button_loc).click()