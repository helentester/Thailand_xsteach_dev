# coding:utf-8
__author__ = 'Helen'
'''
description:包裹页面：即可以把课程加入购物车的页面
'''
from selenium.webdriver.common.by import By
from src.common.Base_Page import BasePage


class package_page(BasePage):
    # 定位器
    pushCart_button_loc = (By.CSS_SELECTOR, '#pushCart')
    goPay_button_loc = (By.CSS_SELECTOR, '#goPay')

    # 点击"去结算"按钮
    def click_goPay_button(self):
        self.find_element(*self.goPay_button_loc).click()
