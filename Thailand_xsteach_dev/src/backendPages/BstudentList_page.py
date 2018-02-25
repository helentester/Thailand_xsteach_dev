# coding:utf-8
__author__ = 'Helen'
'''
description:学员管理页面
'''
from src.common.Base_Page import BasePage
from selenium.webdriver.common.by import By


class BstudentList_page(BasePage):
    # 定位器
    insert_button_loc = (By.CSS_SELECTOR, ".btn.btn-default[href='/users/create']")     # 添加学员按钮
    student_count_loc = (By.CSS_SELECTOR, ".summary>b:nth-child(2)")    # 学员条数

    # 点击添加学员按钮
    def click_insert_button(self):
        self.find_element(*self.insert_button_loc).click()

    # 获取学员记录数
    def get_student_count(self):
        return self.find_element(*self.student_count_loc).text
