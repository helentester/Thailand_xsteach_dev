# coding:utf-8
__author__ = 'Helen'
'''
description:视频列表页面
入口：课程管理－VIP\公开课程－视频录播
'''
from selenium.webdriver.common.by import By
from src.common.Base_Page import BasePage


class BvideoList_page(BasePage):
    # 定位器
    insert_button_loc = (By.CSS_SELECTOR, '.hd>.btn.btn-default')
    videoName_at_firstLine_loc = (By.XPATH, ".//*[@id='period-sortable']/table/tbody/tr[1]/td[2]")
    video_table_loc = (By.CSS_SELECTOR, ".table.table-striped.table-bordered")  # 视频列表table
    update_VIPVideo_link_loc = (By.XPATH, ".//*[@id='period-sortable']/table/tbody/tr[1]/td[7]/a[1]")    # VIP课程的视频列表，第一行第的编辑按钮
    update_openVideo_link_loc = (By.XPATH, ".//*[@id='period-sortable']/table/tbody/tr/td[6]/a[1]")     # 公开课程的视频列表，第一行的编辑按钮

    # 点击新增视频按钮
    def click_insert_button(self):
        self.find_element(*self.insert_button_loc).click()

    # 获取第一行视频的视频名称
    def get_videoName_at_firstLine(self):
        return self.find_element(*self.videoName_at_firstLine_loc).text

    # 点击VIP课程下的视频列表，编辑按钮
    def click_update_VIPvideo_link(self):
        self.find_element(*self.update_VIPVideo_link_loc).click()

    # 点击公开课程下的视频列表，编辑按钮
    def click_update_openVideo_link(self):
        self.find_element(*self.update_openVideo_link_loc).click()

    # 获第一行课时的“试学”状态
    def get_free_statue(self):
        table = self.find_element(*self.video_table_loc)
        row = table.find_elements(By.TAG_NAME, "tr")
        cols = row[1].find_elements(By.TAG_NAME, "td")
        return cols[5].text
