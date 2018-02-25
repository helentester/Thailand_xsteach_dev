# coding:utf-8
__author__ = 'Helen'
'''
description:广告组列表页面
'''
from selenium.webdriver.common.by import By
from src.common.Base_Page import BasePage


class BadGroupList_page(BasePage):
    # 定位器
    add_button_loc = (By.CSS_SELECTOR, ".btn.btn-default")  # 添加广告组按钮
    adGroup_count_loc = (By.CSS_SELECTOR, ".summary>b:nth-child(2)")    # 广告组列表记录数
    adGroup_name_loc = (By.XPATH, ".//*[@id='w0']/table/tbody/tr[1]/td[2]")    # 第一行广告组的名称
    update_link_loc = (By.XPATH, ".//*[@id='w0']/table/tbody/tr[1]/td[4]/a[1]")     # 第一行编辑链接
    delete_link_loc = (By.XPATH, ".//*[@id='w0']/table/tbody/tr[1]/td[4]/a[2]")     # 第一行删除链接
    delete_sure_button_loc = (By.CSS_SELECTOR, ".layui-layer-btn0")     # 确定删除按钮

    # 点击添加广告组按钮
    def click_add_button(self):
        self.find_element(*self.add_button_loc).click()

    # 获取广告组记录数
    def get_adGroup_count(self):
        return self.find_element(*self.adGroup_count_loc).text

    # 获取第一行的广告组名称
    def get_adGroup_name(self):
        return self.find_element(*self.adGroup_name_loc).text

    # 点击第一行编辑链接
    def click_update_link(self):
        self.find_element(*self.update_link_loc).click()

    # 点击第一行删除链接
    def click_delete_link(self):
        self.find_element(*self.delete_link_loc).click()

    # 点击确定删除按钮
    def click_delete_sure_button(self):
        self.find_element(*self.delete_sure_button_loc).click()
