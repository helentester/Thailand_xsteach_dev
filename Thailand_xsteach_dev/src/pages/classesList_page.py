# coding:utf-8
__author__ = 'Helen'
'''
description:课程列表页面
'''
from src.common.Base_Page import BasePage
from selenium.webdriver.common.by import By

class classesList_page(BasePage):
    # 定位器
    vip_classList_loc = (By.CSS_SELECTOR, ".courseNav.mt30.mb20>li>a[href='/course/index?type=V']")
    vip_class1_loc = (By.CSS_SELECTOR, '.courseList>li:nth-child(1)>a')

    # 点击VIP课程标签页面
    def click_vip_classList(self):
        self.find_element(*self.vip_classList_loc).click()

    # 点击VIP课程第一个
    def click_vip_class1(self):
        self.find_element(*self.vip_class1_loc).click()

    # 获取VIP课程第一个课的href属性
    def get_vip_class1_href(self):
        return self.find_element(*self.vip_class1_loc).get_attribute('href')



