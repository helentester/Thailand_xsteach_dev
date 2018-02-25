# coding:utf-8
__author__ = 'Helen'
'''
description:老师管理列表
'''
from src.common.Base_Page import BasePage
from selenium.webdriver.common.by import By


class BteacherList_page(BasePage):
    # 定位器
    add_button_loc = (By.CSS_SELECTOR, ".btn.btn-default")
    teacher_count_loc = (By.CSS_SELECTOR, ".summary>b:nth-child(2)")

    # 点击新增主讲老师按钮
    def click_add_button(self):
        self.find_element(*self.add_button_loc).click()

    # 获取老师记录条数
    def get_teacher_count(self):
        return self.find_element(*self.teacher_count_loc).text

