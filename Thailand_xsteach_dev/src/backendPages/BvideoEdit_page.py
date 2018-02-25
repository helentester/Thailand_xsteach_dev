# coding:utf-8
__author__ = 'Helen'
'''
description:视频编辑页面
'''
from selenium.webdriver.common.by import By
from src.common.Base_Page import BasePage
import time


class BvideoEdit_page(BasePage):
    # 定位器
    classTheme_loc = (By.CSS_SELECTOR, '#courserecording-class_theme')
    videoID_loc = (By.CSS_SELECTOR, '#courserecording-video_id')
    video_length_loc = (By.CSS_SELECTOR, '#video-length')
    free_statue_loc = (By.CSS_SELECTOR, "#courserecording-trial>label>input")   # 试学状态
    submit_button_loc = (By.CSS_SELECTOR, '.btn.btn-primary.offset')

    # 输入课时
    def input_classTheme(self, classTheme):
        self.send_keys(classTheme,*self.classTheme_loc)

    # 输入视频ID
    def input_videoID(self, videoID):
        self.send_keys(videoID,*self.videoID_loc)

    # 点击获取视频时长
    def click_videoLength(self):
        self.find_element(*self.video_length_loc).click()
        time.sleep(2)

    # 点击试学状态
    def click_free_statue(self):
        self.find_element(*self.free_statue_loc).click()

    # 点击提交按钮
    def click_submitButton(self):
        self.find_element(*self.submit_button_loc).click()

