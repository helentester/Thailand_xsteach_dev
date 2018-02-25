# coding:utf-8
__author__ = 'Helen'
'''
description:学员管理测试
'''
import unittest
import public_module
from src.common.data_generating import data_generating
from src.backendPages import BsiteMenu_page, BstudentList_page, BstudentEdit_page


class test_bankend_studentManage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.PM = public_module.public_module()
        cls.data_generate = data_generating()
        # 登录
        cls.driver = cls.PM.Blogin()
        # 后台主页
        cls.BsiteMenu_page = BsiteMenu_page.BsiteMenu_page(cls.driver)
        cls.BsiteMenu_page.click_studentIndex()

    def test_insert_student(self):
        '''添加学员'''
        # 学员列表页面
        self.BstudentList_page = BstudentList_page.BstudentList_page(self.driver)
        student_count = self.BstudentList_page.get_student_count()
        self.BstudentList_page.click_insert_button()
        # 编辑学员页面
        self.BstudentEdit_page = BstudentEdit_page.BstudentEdit_page(self.driver)
        studentName = 'student'+str(self.data_generate.create_randomInt(0,999))
        self.BstudentEdit_page.input_studentName(studentName)
        self.BstudentEdit_page.input_password('123456')     # 默认123456
        self.BstudentEdit_page.input_email(studentName+'@test.com')
        self.BstudentEdit_page.click_submit_button()
        self.assertTrue(int(student_count)+1 == int(self.BstudentList_page.get_student_count()))

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__ == '__main__':
    unittest.main()
