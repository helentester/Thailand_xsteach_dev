# coding:utf-8
__author__ = 'Helen'
'''
description:确认订单页面
'''
from src.common.Base_Page import BasePage
from selenium.webdriver.common.by import By

class BorderConfirm_page(BasePage):
    # 定位器
    remark_loc = (By.CSS_SELECTOR, '#order-remark') # 操作备注
    submit_button_loc = (By.CSS_SELECTOR, '.btn.btn-primary.offset')    # 提交按钮

    # 输入操作备注
    def input_remark(self, order_remark):
        self.send_keys(order_remark,*self.remark_loc)

    # 点击提交按钮
    def click_submit_button(self):
        self.find_element(*self.submit_button_loc).click()
