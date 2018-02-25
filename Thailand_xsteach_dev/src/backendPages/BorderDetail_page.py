# coding:utf-8
__author__ = 'Helen'
'''
description:订单详细页面
'''
from selenium.webdriver.common.by import By
from src.common.Base_Page import BasePage

class BorderDetail_page(BasePage):
    # 定位器
    confirm_button_loc = (By.XPATH, ".//*[@id='main']/div/div[2]/div[2]/div/div[1]/h3[1]/a")    # 确认按钮
    cancel_button_loc = (By.XPATH, ".//*[@id='main']/div/div[2]/div[1]/div[1]/div[1]/h3/a")     # 取消按钮
    updateOrder_button_loc = (By.XPATH, ".//*[@id='main']/div/div[2]/div[2]/div/div[1]/h3[2]/a")    # 修改订单信息按钮
    confirm_status_loc = (By.XPATH, ".//*[@id='main']/div/div[2]/div[1]/div[1]/div[2]/dl/dd[2]")     # 订单确认状态
    amount_paid_loc = (By.XPATH, ".//*[@id='main']/div/div[2]/div[2]/div/div[2]/dl/dd[2]")      # 实际支付金额

    # 点击确认按钮
    def click_confirm_button(self):
        self.find_element(*self.confirm_button_loc).click()

    # 点击取消按钮
    def click_cancel_button(self):
        self.find_element(*self.cancel_button_loc).click()

    # 点击修改订单信息按钮
    def click_updateOrder_button(self):
        self.find_element(*self.updateOrder_button_loc).click()

    # 返回订单确认状态
    def get_confirm_status(self):
        return (self.find_element(*self.confirm_status_loc).text.strip().lstrip())[3:]

    # 返回实际支付金额
    def get_amount_paid(self):
        return (self.find_element(*self.amount_paid_loc).text.strip().lstrip())[7:]
