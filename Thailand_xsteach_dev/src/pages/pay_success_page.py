# coding:utf-8
__author__ = 'Helen'
'''
description:支付成功页面
'''
from src.common.Base_Page import BasePage
from selenium.webdriver.common.by import By


class paySuccess_page(BasePage):
    # 定位器
    backIndex_button_loc = (By.CSS_SELECTOR, '.button.btn-blue')

    # 判定“返回首页”按钮是否存在
    def backIndex_button_display(self):
        return self.find_element(*self.backIndex_button_loc).is_displayed()
