# coding:utf-8
__author__ = 'Helen'
'''
description:课程详细查看页面
'''
from src.common.Base_Page import BasePage
from selenium.webdriver.common.by import By


class class_page(BasePage):
    # 定位器
    buy_button_loc = (By.CLASS_NAME,'btn-green')

    def click_buy_button(self):
        self.find_element(*self.buy_button_loc).click()
