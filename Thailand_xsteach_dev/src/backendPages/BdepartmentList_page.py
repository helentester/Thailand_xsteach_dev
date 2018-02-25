# coding:utf-8
__author__ = 'Helen'
'''
description:部门管理页面
'''
from src.common.Base_Page import BasePage
from selenium.webdriver.common.by import By


class BdepartmentList_page(BasePage):
    # 定位器
    add_button_loc = (By.CSS_SELECTOR, ".btn.btn-default")
    department_count_loc = (By.CSS_SELECTOR, ".summary>b:nth-child(2)")

    # 点击添加部门按钮
    def click_add_button(self):
        self.find_element(*self.add_button_loc).click()

    # 获取部门记录数
    def get_department_count(self):
        return self.find_element(*self.department_count_loc).text
