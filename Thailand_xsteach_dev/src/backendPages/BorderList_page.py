# coding:utf-8
__author__ = 'Helen'
'''
description:订单管理页面
'''
from src.common.Base_Page import BasePage
from selenium.webdriver.common.by import By


class BorderList_page(BasePage):
    # 定位器
    status_loc = (By.CSS_SELECTOR, ".form-wrap>select>option[value='1']")   # 状态下拉框（选择待审核）
    search_button_loc = (By.CSS_SELECTOR, ".btn.btn-default.ml10")  # 查询按钮
    detailLink_at_firstLine_loc = (By.XPATH, ".//*[@id='w2']/table/tbody/tr[1]/td[9]/a")    # 第一行的“订单详情”

    # 选择状态
    def search_status(self):
        self.find_element(*self.status_loc).click()

    # 点击查询按钮
    def click_search_button(self):
        self.find_element(*self.search_button_loc).click()

    # 点击第一行的“订单详情”
    def click_detailLink_at_firstLine(self):
        self.find_element(*self.detailLink_at_firstLine_loc).click()
