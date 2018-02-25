# coding:utf-8
__author__ = 'Helen'
'''
description:
'''
import unittest,time
import public_module
from src.common.data_generating import data_generating
from src.backendPages import BsiteMenu_page, BorderList_page,BorderDetail_page, BorderConfirm_page, \
    BorderUpdate_page, BorderCancel_page


class test_bankend_orderManage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.PM = public_module.public_module()
        cls.data_generate = data_generating()
        # 登录
        cls.driver = cls.PM.Blogin()
        # 后台主页
        cls.BsiteMenu_page = BsiteMenu_page.BsiteMenu_page(cls.driver)
        cls.BsiteMenu_page.click_orderIndex()
        # 订单列表
        cls.BorderList_page = BorderList_page.BorderList_page(cls.driver)
        cls.BorderList_page.search_status()
        cls.BorderList_page.click_search_button()
        cls.BorderList_page.click_detailLink_at_firstLine()

    def setUp(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def test_01orderConfirm(self):
        '''确认订单'''
        # 订单详细页面
        self.BorderDetail_page = BorderDetail_page.BorderDetail_page(self.driver)
        self.BorderDetail_page.click_confirm_button()
        # 确认订单页面
        self.BorderConfirm_page = BorderConfirm_page.BorderConfirm_page(self.driver)
        self.BorderConfirm_page.img_screenshot('confirm order auto')
        self.BorderConfirm_page.click_submit_button()
        self.assertEqual(u'已确认', self.BorderDetail_page.get_confirm_status())

    def test_02updateConfirm(self):
        '''修改订单信息'''
        # 订单详细页面
        self.BorderDetail_page = BorderDetail_page.BorderDetail_page(self.driver)        #
        self.BorderDetail_page.click_updateOrder_button()
        # 修改订单信息页面
        self.BorderUpdate_page = BorderUpdate_page.BorderUpdate_page(self.driver)
        amount_paid = self.data_generate.create_randomFloat(0, 9999, 2)
        self.BorderUpdate_page.input_amount_paid(str(amount_paid))
        self.BorderUpdate_page.input_remark('update order auto')
        self.BorderUpdate_page.click_submit_button()
        self.assertTrue(amount_paid == float(self.BorderDetail_page.get_amount_paid()))

    def test_03cancelOrder(self):
        '''取消订单'''
        # 订单详细页面
        self.BorderDetail_page = BorderDetail_page.BorderDetail_page(self.driver)
        self.BorderDetail_page.click_cancel_button()
        # 订单取消页面
        self.BorderCancel_page = BorderCancel_page.BorderCancel_page(self.driver)
        self.BorderCancel_page.input_remark('cancel order auto')
        self.BorderCancel_page.click_submit_button()
        self.assertEqual(u'已取消',self.BorderDetail_page.get_confirm_status())
