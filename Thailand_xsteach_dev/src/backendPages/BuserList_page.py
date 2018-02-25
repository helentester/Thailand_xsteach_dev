# coding:utf-8
__author__ = 'Helen'
'''
description:用户管理页面
'''
from src.common.Base_Page import BasePage
from selenium.webdriver.common.by import By


class BuserList_page(BasePage):
    # 定位器
    add_button_loc = (By.CSS_SELECTOR, ".btn.btn-default")  # 新增管理员按钮
    user_count_loc = (By.CSS_SELECTOR, ".summary>b:nth-child(2)")   # 用户记录数

    # 点击新增管理按钮
    def click_add_button(self):
        self.find_element(*self.add_button_loc).click()

    # 获取用户记录数
    def get_user_count(self):
        return self.find_element(*self.user_count_loc).text
