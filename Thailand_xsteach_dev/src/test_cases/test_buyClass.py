# coding:utf-8
__author__ = 'Helen'
'''
description:测试购买课程的主要业务流：打开首页－登录－打开课程页－打开VIP标签页－点击第一个VIP课程－
        “我要报名”－“去结算”－“去结算”－“提交订单”－输入转账人信息，提交－断言最后提交成功的页面
'''
import unittest,time
from selenium import webdriver
from config import globalparameter as gl
from src.pages.index_page import index_page
from src.pages.login_page import login_page
from src.pages.classesList_page import classesList_page
from src.pages.class_page import class_page
from src.pages.package_page import package_page
from src.pages.cart_page import cart_page
from src.pages.submitOrder_page import submitOrder_page
from src.pages.payerInfo_page import payerInfo_page
from src.pages.pay_success_page import paySuccess_page
from src.common.window_transaction import window_transaction
from src.common.log import log


class test_buyClass(unittest.TestCase):
    def setUp(self):
        profile_directory = r'C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\vlq8tn8d.default'
        profile = webdriver.FirefoxProfile(profile_directory)
        self.driver = webdriver.Firefox(profile)
        self.index_page = index_page(self.driver)
        self.window_transaction = window_transaction()
        self.mylog = log()

    def test_buyClass(self):
        '''测试购买课程的业务流'''
        try:
            self.index_page.open()
            # time.sleep(3)
            h = self.driver.current_window_handle
            self.index_page.click_login_linck()
            time.sleep(3)
            self.driver.close()
            all_h = self.driver.window_handles
            login_window_handle = self.window_transaction.window_change(all_h,h)
            self.mylog.debug(login_window_handle)

            # 切换到新窗口,登录操作
            self.driver.switch_to.window(login_window_handle)
            self.login_page = login_page(self.driver)
            self.login_page.input_username('test@qq.com')
            self.login_page.input_password('123456')
            self.login_page.click_login_button()
            self.index_page = index_page(self.driver)
            self.assertTrue(self.index_page.user_icon())

            # 打开课程列表页面
            self.index_page.click_classes_link()
            # time.sleep(2)
            self.classesList_page = classesList_page(self.driver)
            self.classesList_page.click_vip_classList()
            old_handle = self.driver.current_window_handle
            class_href = self.classesList_page.get_vip_class1_href()
            self.mylog.debug(class_href)

            # 打开第一个VIP课程
            self.classesList_page.click_vip_class1()
            time.sleep(2)
            all_h = self.driver.window_handles
            self.driver.close()
            class_window_handle = self.window_transaction.window_change(all_h,old_handle)
            self.driver.switch_to.window(class_window_handle)
            self.class_page = class_page(self.driver)
            time.sleep(2)
            self.class_page.click_buy_button()

            # 包裹页面
            self.package_page = package_page(self.driver)
            self.package_page.click_goPay_button()

            # 购物车页面
            self.cart_page = cart_page(self.driver)
            self.cart_page.click_delete()
            self.cart_page.click_goPay_button()

            # 提交订单页面
            self.submitOrder_page = submitOrder_page(self.driver)
            self.submitOrder_page.click_submitOrder_button()

            # 填写转账人信息页面
            self.payerInfo_page = payerInfo_page(self.driver)
            self.payerInfo_page.input_payer_name('autoTester')
            self.payerInfo_page.input_payer_phone('1388888888')
            self.payerInfo_page.upload_file(gl.img_for_test_path)
            self.payerInfo_page.click_submit_button()

            # 提交成功页面
            self.paySuccess_page = paySuccess_page(self.driver)
            self.assertTrue(self.paySuccess_page.backIndex_button_display())
        except Exception as e:
            raise e

    def tearDown(self):
        self.driver.close()
        # pass