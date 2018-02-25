# coding:utf-8
__author__ = 'Helen'
'''
description:修改订单支付信息页面
'''
from src.common.Base_Page import BasePage
from selenium.webdriver.common.by import By


class BorderUpdate_page(BasePage):
    # 定位器
    amount_paid_loc = (By.CSS_SELECTOR, '#order-paid_amount')   # 实际支付金额
    remark_loc = (By.CSS_SELECTOR, '#order-remark')     # 操作备注
    submit_button_loc = (By.CSS_SELECTOR, ".btn.btn-primary.offset")    # 提交按钮

    # 输入实际支付金额
    def input_amount_paid(self, amount_paid):
        self.send_keys(amount_paid,*self.amount_paid_loc)

    # 输入操作备注
    def input_remark(self, order_remark):
        self.send_keys(order_remark,*self.remark_loc)

    # 点击提交按钮
    def click_submit_button(self):
        self.find_element(*self.submit_button_loc).click()
