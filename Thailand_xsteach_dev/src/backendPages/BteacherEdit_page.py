# coding:utf-8
__author__ = 'Helen'
'''
description:编辑老师页面
'''
from src.common.Base_Page import BasePage
from selenium.webdriver.common.by import By
import time


class BteacherEdit_page(BasePage):
    # 定位器
    teacher_name_loc = (By.CSS_SELECTOR, '#teacher-name')
    teacherImg_file_loc = (By.CSS_SELECTOR, ".webuploader-element-invisible")
    uploadImg_button_loc = (By.CSS_SELECTOR, "#uploader-teacher-picture-upload")
    teacher_intro_loc = (By.CSS_SELECTOR, "#teacher-intro")
    submit_button_loc = (By.CSS_SELECTOR, ".btn.btn-primary.offset")

    # 输入老师名称
    def input_teacher_name(self, teacher_name):
        self.send_keys(teacher_name, *self.teacher_name_loc)

    # 输入头像
    def input_teacherImg_file(self, teacherImg):
        self.find_element(*self.teacherImg_file_loc).send_keys(teacherImg)
        self.find_element(*self.uploadImg_button_loc).click()
        time.sleep(2)

    # 输入老师简介
    def input_teacher_intro(self, teacher_intro):
        self.send_keys(teacher_intro,*self.teacher_intro_loc)

    # 点击提交按钮
    def click_submit_button(self):
        self.find_element(*self.submit_button_loc).click()

