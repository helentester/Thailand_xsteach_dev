# coding:utf-8
__author__ = 'Helen'
'''
description:提交订单页面
'''
from src.common.Base_Page import BasePage
from selenium.webdriver.common.by import By


class submitOrder_page(BasePage):
    # 定位器
    submitOrder_button_loc = (By.CSS_SELECTOR, '#submitOrder')  # 提交订单按钮

    # 点击提交订单按钮
    def click_submitOrder_button(self):
        self.find_element(*self.submitOrder_button_loc).click()