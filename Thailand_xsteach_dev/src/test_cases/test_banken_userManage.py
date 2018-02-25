# coding:utf-8
__author__ = 'Helen'
'''
description:用户管理测试
'''
import unittest
import public_module
from src.backendPages import BuserList_page, BuserEdit_page, BsiteMenu_page, BdepartmentList_page, BdepartmentEdit_page
from src.common import data_generating


class test_banken_userManage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.PM = public_module.public_module()
        cls.data_generate = data_generating.data_generating()
        # 登录
        cls.driver = cls.PM.Blogin()

    def test_insert_user(self):
        '''添加管理员用户'''
        # 后台主页
        self.BsiteMenu_page = BsiteMenu_page.BsiteMenu_page(self.driver)
        self.BsiteMenu_page.click_userIndex()
        # 用户管理页面
        self.BuserList_page = BuserList_page.BuserList_page(self.driver)
        user_count = self.BuserList_page.get_user_count()
        self.BuserList_page.click_add_button()
        # 编辑用户页面
        self.BuserEdit_page = BuserEdit_page.BuserEdit_page(self.driver)
        self.BuserEdit_page.input_mobile(self.data_generate.create_PhoneNo())
        self.BuserEdit_page.input_password('123456')
        user_name = 'user_'+str(self.data_generate.create_randomInt(0,999))
        self.BuserEdit_page.input_name(user_name)
        self.BuserEdit_page.input_email(user_name+'@test.com')
        self.BuserEdit_page.click_department()
        self.BuserEdit_page.click_submit_button()
        self.assertTrue(int(user_count)+1 == int(self.BuserList_page.get_user_count()))

    def test_insert_department(self):
        '''新增部门'''
        # 后台主页
        self.BsiteMenu_page = BsiteMenu_page.BsiteMenu_page(self.driver)
        self.BsiteMenu_page.click_departmentIndex()
        # 部门管理页面
        self.BdepartmentList_page = BdepartmentList_page.BdepartmentList_page(self.driver)
        department_count = self.BdepartmentList_page.get_department_count()
        self.BdepartmentList_page.click_add_button()
        # 编辑部门页面
        self.BdepartmentEdit_page = BdepartmentEdit_page.BdepartmentEdit_page(self.driver)
        self.BdepartmentEdit_page.input_department_name('department_'+str(self.data_generate.create_randomInt(0,990)))
        self.BdepartmentEdit_page.click_submit_button()
        self.assertTrue(int(department_count)+1 == int(self.BdepartmentList_page.get_department_count()))

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__ == '__main__':
    unittest.main()


