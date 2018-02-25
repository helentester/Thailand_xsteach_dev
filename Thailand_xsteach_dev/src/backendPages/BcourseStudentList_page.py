# coding:utf-8
__author__ = 'Helen'
'''
description:课程学员管理列表页面
'''
from src.common.Base_Page import BasePage
from selenium.webdriver.common.by import By


class BcourseStudentList(BasePage):
    # 定位器
    addStudent_button_loc = (By.CSS_SELECTOR, '.btn.btn-default')   # 添加学员按钮
    studentUID_at_firstLine_loc = (By.XPATH, ".//*[@id='w0']/table/tbody/tr[1]/td[1]")  # 第一行学员的UID
    update_link_loc = (By.XPATH, ".//*[@id='w0']/table/tbody/tr/td[9]/a[1]")    # 第一行编辑按钮

    # 点击添加学员
    def click_addStudent_button(self):
        self.find_element(*self.addStudent_button_loc).click()

    # 获取第一行学员的UID
    def get_studentUID_at_firstLine(self):
        return self.find_element(*self.studentUID_at_firstLine_loc).text

    # 点击第一行学员的编辑按钮
    def click_update_button(self):
        self.find_element(*self.update_link_loc).click()
