# coding:utf-8
__author__ = 'Helen'
'''
description:广告管理列表页面
'''
from selenium.webdriver.common.by import By
from src.common.Base_Page import BasePage


class BadList_page(BasePage):
    # 定位器
    ad_group_index_loc = (By.CSS_SELECTOR, ".btn.btn-default[href='/ad-group/index']")  # 广告组管理按钮
    Add_ad_buttong_loc = (By.CSS_SELECTOR, ".btn.btn-default[href='/ad/create']")   # 添加广告按钮
    ad_count_loc = (By.CSS_SELECTOR, ".summary>b:nth-child(2)")     # 广告列表条数
    ad_title_loc = (By.XPATH, ".//*[@id='period-sortable']/table/tbody/tr[1]/td[3]")     # 第一行广告标题
    update_link_loc = (By.XPATH, ".//*[@id='period-sortable']/table/tbody/tr[1]/td[8]/a[1]")    # 第一行编辑按钮
    delete_link_loc = (By.XPATH, ".//*[@id='period-sortable']/table/tbody/tr[1]/td[8]/a[2]")    # 第一行删除链接
    delete_sure_loc = (By.CSS_SELECTOR, ".layui-layer-btn0")    # 删除确定按钮

    # 点击广告组管理按钮
    def click_ad_group_index(self):
        self.find_element(*self.ad_group_index_loc).click()

    # 点击添加广告按钮
    def click_Add_ad_button(self):
        self.find_element(*self.Add_ad_buttong_loc).click()

    # 获取广告列表条数
    def get_ad_count(self):
        return self.find_element(*self.ad_count_loc).text

    # 获取第一行广告标题
    def get_ad_title(self):
        return self.find_element(*self.ad_title_loc).text

    # 点击第一行编辑按钮
    def click_update_link(self):
        self.find_element(*self.update_link_loc).click()

    # 点击第一行删除链接
    def click_delete_link(self):
        self.find_element(*self.delete_link_loc).click()

    # 点击删除确定按钮
    def click_delete_sure(self):
        self.find_element(*self.delete_sure_loc).click()

