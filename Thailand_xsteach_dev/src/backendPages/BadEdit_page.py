# coding:utf-8
__author__ = 'Helen'
'''
description:编辑广告页面
'''
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from src.common.Base_Page import BasePage
import time


class BadEdit_page(BasePage):
    # 定位器
    title_loc = (By.CSS_SELECTOR, '#ad-title')  # 标题
    ad_group_loc = (By.CSS_SELECTOR, "#ad-group_id>option:nth-child(3)")    # 广告组
    ad_type_loc = (By.XPATH, ".//*[@id='ad-type']")     # 广告类型
    ad_videoID_loc = (By.CSS_SELECTOR, "#ad-video_id")  # 视频ID
    ad_imgFile_loc = (By.CSS_SELECTOR, ".webuploader-element-invisible")    # 图片路径
    ad_imgUpload_loc = (By.CSS_SELECTOR, "#uploader-ad-image-upload")   # 上传图片按钮
    ad_imgLink_loc = (By.CSS_SELECTOR, "#ad-link")  # 图片链接
    ad_startTime_loc = (By.CSS_SELECTOR, "#ad-start_time")  # 开始时间
    js_startTime = 'document.getElementById("ad-start_time").removeAttribute("readonly");'
    ad_endTime_loc = (By.CSS_SELECTOR, "#ad-end_time")  # 结束时间
    js_endTime = 'document.getElementById("ad-end_time").removeAttribute("readonly");'
    statue_forbidden_loc = (By.XPATH, ".//*[@id='ad-status']/label[2]/input")   # 禁用状态
    submit_button_loc = (By.CSS_SELECTOR, ".btn.btn-primary.offset")    # 提交按钮

    # 输入标题
    def input_title(self, ad_title):
        self.send_keys(ad_title, *self.title_loc)

    def click_title(self):
        self.find_element(*self.title_loc).click()

    # 选择广告组
    def click_ad_group(self):
        self.find_element(*self.ad_group_loc).click()

    # 选择广告类型
    def select_ad_type(self, type_value):
        s = self.find_element(*self.ad_type_loc)
        Select(s).select_by_value(type_value)
        s.click()

    # 获取当前广告类型的value值
    def get_ad_type(self):
        return self.find_element(*self.ad_type_loc).get_attribute("value")

    # 输入视频ID
    def input_VideoID(self, videoID):
        self.send_keys(videoID, *self.ad_videoID_loc)

    # 上传图片
    def upload_imgFile(self, imgFile):
        self.find_element(*self.ad_imgFile_loc).send_keys(imgFile)
        self.find_element(*self.ad_imgUpload_loc).click()
        time.sleep(2)

    # 输入图片链接
    def input_imgLink(self, img_link):
        self.send_keys(img_link, *self.ad_imgLink_loc)

    # 输入开始时间
    def input_startTime(self, startTime):
        self.execute_JS(self.js_startTime)
        self.send_keys(startTime, *self.ad_startTime_loc)

    # 输入结束时间
    def input_endTime(self, endTime):
        self.execute_JS(self.js_endTime)
        self.send_keys(endTime, *self.ad_endTime_loc)

    # 点击禁用状态
    def click_statue_forbidden(self):
        self.find_element(*self.statue_forbidden_loc).click()

    # 点击提交按钮
    def click_submit_button(self):
        self.find_element(*self.submit_button_loc).click()
