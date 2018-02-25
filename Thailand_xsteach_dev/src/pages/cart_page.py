# coding:utf-8
__author__ = 'Helen'
'''
description:购物车页面
'''
from selenium.webdriver.common.by import By
from src.common.Base_Page import BasePage

class cart_page(BasePage):
    # 定位器
    goPay_button_loc = (By.ID, 'goPay')  # 去结算
    delete_loc = (By.CSS_SELECTOR, '.fc-red.cursor.delete')

    # 点击“删除”
    def click_delete(self):
        self.find_element(*self.delete_loc).click

    # 点击“去结算”
    def click_goPay_button(self):
        self.find_element(*self.goPay_button_loc).click()
