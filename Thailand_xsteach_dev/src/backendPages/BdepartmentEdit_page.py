# coding:utf-8
__author__ = 'Helen'
'''
description:部门编辑页面
'''
from src.common.Base_Page import BasePage
from selenium.webdriver.common.by import By


class BdepartmentEdit_page(BasePage):
    #  定位器
    department_name_loc = (By.CSS_SELECTOR, "#department-name")
    submit_buttong_loc = (By.CSS_SELECTOR, ".btn.btn-primary.offset")

    # 输入部门名称
    def input_department_name(self, department_name):
        self.send_keys(department_name, *self.department_name_loc)

    # 点击提交按钮
    def click_submit_button(self):
        self.find_element(*self.submit_buttong_loc).click()
