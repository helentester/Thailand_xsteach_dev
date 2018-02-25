# coding:utf-8
__author__ = 'Helen'
'''
description:老师管理模块测试
'''
import unittest
from config import globalparameter as gl
from src.common.data_generating import data_generating
from src.backendPages import BsiteMenu_page, BteacherList_page, BteacherEdit_page
import public_module


class test_bankend_teacherManage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.PM = public_module.public_module()
        cls.data_generate = data_generating()
        # 登录
        cls.driver = cls.PM.Blogin()

    def test_insert_teacher(self):
        '''新增老师'''
        # 后台主页面
        self.BsiteMenu_page = BsiteMenu_page.BsiteMenu_page(self.driver)
        self.BsiteMenu_page.click_teacherIndex()
        # 老师管理页面
        self.BteacherList_page = BteacherList_page.BteacherList_page(self.driver)
        teacher_count = self.BteacherList_page.get_teacher_count()
        self.BteacherList_page.click_add_button()
        # 编辑老师页面
        self.BteacherEdit_page = BteacherEdit_page.BteacherEdit_page(self.driver)
        self.BteacherEdit_page.input_teacher_name('teacher_'+str(self.data_generate.create_randomInt(0, 999)))
        self.BteacherEdit_page.input_teacherImg_file(gl.img_for_test_path)
        self.BteacherEdit_page.input_teacher_intro('insert teacher auto')
        self.BteacherEdit_page.click_submit_button()
        self.assertTrue(int(teacher_count)+1 == int(self.BteacherList_page.get_teacher_count()))

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
