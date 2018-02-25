# coding:utf-8
__author__ = 'Helen'
'''
description:课程学员编辑页面
'''
from src.common.Base_Page import BasePage
from selenium.webdriver.common.by import By


class BcourseStudentEdit_page(BasePage):
    # 定位器
    studentUID_loc = (By.CSS_SELECTOR, '#userhascourse-user_id')
    submit_button_loc = (By.CSS_SELECTOR, '.btn.btn-primary.offset')

    # 输入学员UID
    def input_studentUID(self, studentUID):
        self.send_keys(studentUID, *self.studentUID_loc)

    # 点击提交按钮
    def click_submit_button(self):
        self.find_element(*self.submit_button_loc).click()
