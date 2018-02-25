# coding:utf-8
__author__ = 'Helen'
'''
description:转账人信息页面
'''
from src.common.Base_Page import BasePage
from selenium.webdriver.common.by import By
import time


class payerInfo_page(BasePage):
    # 定位器
    payer_name_loc = (By.CSS_SELECTOR, '#ordertransfer-pay_username')  # 转账人姓名
    payer_phone_loc = (By.CSS_SELECTOR, '#ordertransfer-pay_phone')  # 转账人手机
    upload_file_loc = (By.CSS_SELECTOR, '.webuploader-element-invisible')  # 被隐藏的上传输入框
    upload_button_loc = (By.CSS_SELECTOR, '#uploader-ordertransfer-pay_voucher-upload')  # 开始上传按钮
    submit_button_loc = (By.CSS_SELECTOR, '.cursor.btn-blue')  # 提交按钮

    # 输入转账人姓名
    def input_payer_name(self,payer_name):
        self.send_keys(payer_name,*self.payer_name_loc)

    # 输入转账人手机
    def input_payer_phone(self,payer_phone):
        self.send_keys(payer_phone,*self.payer_phone_loc)

    # 上传转账凭证
    def upload_file(self,file_path):
        self.find_element(*self.upload_file_loc).send_keys(file_path)
        self.find_element(*self.upload_button_loc).click()
        time.sleep(2)

    # 点击提交按钮
    def click_submit_button(self):
        self.find_element(*self.submit_button_loc).click()
