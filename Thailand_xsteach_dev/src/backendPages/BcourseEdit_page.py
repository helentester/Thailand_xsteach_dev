# coding:utf-8
__author__ = 'Helen'
'''
description:编辑VIP\公开课程页面
'''
from src.common.Base_Page import BasePage
from selenium.webdriver.common.by import By
import time


class BcourseEdit_page(BasePage):
    # 定位器
    course_name_loc = (By.CSS_SELECTOR, '#course-name')
    course_category_loc = (By.CSS_SELECTOR, "#course-category_id>option[value='1']")    # 默认选择第一个分类
    course_teacher_loc = (By.CSS_SELECTOR, "#course-teacher_id>option[value='1']")  # 默认选择第一个老师
    course_term_loc = (By.CSS_SELECTOR, "#course-term>option[value='1']")   # 默认选择第一个：一个月
    uploader_littleImg_loc = (By.CSS_SELECTOR, '#uploader-course-cover-pick>div:nth-child(2)>input')
    uploader_littleButton_loc = (By.CSS_SELECTOR, '#uploader-course-cover-upload')
    uploader_bigImg_loc = (By.CSS_SELECTOR, '#uploader-course-big_cover-pick>div:nth-child(2)>input')
    uploader_bigButton_loc = (By.CSS_SELECTOR, '#uploader-course-big_cover-upload')
    course_intro_loc = (By.CSS_SELECTOR, '#course-intro')
    course_price_loc = (By.CSS_SELECTOR, '#course-price')
    statue_notSell_loc = (By.CSS_SELECTOR, "#course-status>label>input[value='1']")  # 下架
    submit_button_loc = (By.CSS_SELECTOR, '.btn.btn-primary.offset')

    # 输入课程名称
    def input_course_name(self, courseName):
        self.send_keys(courseName, *self.course_name_loc)

    # 选择课程分类
    def click_course_category(self):
        self.find_element(*self.course_category_loc).click()

    # 选择老师
    def click_course_teacher(self):
        self.find_element(*self.course_teacher_loc).click()

    # 选择课程有效时间
    def click_course_term(self):
        self.find_element(*self.course_term_loc).click()

    # 上传小图标
    def upload_littleImg(self, littleImg):
        self.find_element(*self.uploader_littleImg_loc).send_keys(littleImg)
        # time.sleep(2)
        self.find_element(*self.uploader_littleButton_loc).click()

    # 上传大图标
    def upload_bigImg(self, bigImg):
        self.find_element(*self.uploader_bigImg_loc).send_keys(bigImg)
        # time.sleep(2)
        self.find_element(*self.uploader_bigButton_loc).click()

    # 输入课程简介
    def input_course_intro(self, course_intro):
        self.send_keys(course_intro, *self.course_intro_loc)

    # 输入课程价格
    def input_course_price(self,course_price):
        self.send_keys(course_price, *self.course_price_loc)

    # 点击下架按钮
    def click_statue_notSell(self):
        self.find_element(*self.statue_notSell_loc).click()

    # 点击提交按钮
    def click_submit_button(self):
        self.find_element(*self.submit_button_loc).click()



