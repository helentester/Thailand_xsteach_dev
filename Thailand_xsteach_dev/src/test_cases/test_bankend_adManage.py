# coding:utf-8
__author__ = 'Helen'
'''
description:广告管理测试
'''
import unittest,time
import public_module
from config import globalparameter as gl
from src.common.data_generating import data_generating
from src.backendPages import BadList_page, BadEdit_page, BsiteMenu_page, BadGroupList_page, BadGroupEdit_page


class test_banken_adManage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.PM = public_module.public_module()
        cls.data_generate = data_generating()
        # 登录
        cls.driver = cls.PM.Blogin()

    def test_01insert_video_ad(self):
        '''添加视频广告'''
        # 后台主页
        self.BsiteMenu_page = BsiteMenu_page.BsiteMenu_page(self.driver)
        self.BsiteMenu_page.click_adIndex()
        # 广告列表页面
        self.BadList_page = BadList_page.BadList_page(self.driver)
        ad_count = self.BadList_page.get_ad_count()
        self.BadList_page.click_Add_ad_button()
        # 编辑广告页面
        self.BadEdit_page = BadEdit_page.BadEdit_page(self.driver)
        self.BadEdit_page.input_title('videoAd'+str(self.data_generate.create_randomInt(0, 999)))
        self.BadEdit_page.click_ad_group()
        self.BadEdit_page.select_ad_type('0')
        self.BadEdit_page.input_VideoID('9031868222894357044')
        self.BadEdit_page.input_startTime(str(self.data_generate.create_time_today()))
        self.BadEdit_page.input_endTime(str(self.data_generate.creat_time_nextMonth()))
        self.BadEdit_page.click_title()
        self.BadEdit_page.click_submit_button()
        self.assertTrue(int(ad_count)+1 == int(self.BadList_page.get_ad_count()))

    def test_02insert_img_ad(self):
        '''添加图片广告'''
        # 后台主页
        self.BsiteMenu_page = BsiteMenu_page.BsiteMenu_page(self.driver)
        self.BsiteMenu_page.click_adIndex()
        # 广告列表页面
        self.BadList_page = BadList_page.BadList_page(self.driver)
        ad_count = self.BadList_page.get_ad_count()
        self.BadList_page.click_Add_ad_button()
        # 编辑广告页面
        self.BadEdit_page = BadEdit_page.BadEdit_page(self.driver)
        self.BadEdit_page.input_title('imgAd'+str(self.data_generate.create_randomInt(0, 999)))
        self.BadEdit_page.click_ad_group()
        self.BadEdit_page.select_ad_type('1')
        self.BadEdit_page.input_imgLink(r'http://www.cnblogs.com/helenMemery/')
        self.BadEdit_page.upload_imgFile(gl.img_for_test_path)
        self.BadEdit_page.input_startTime(str(self.data_generate.create_time_today()))
        self.BadEdit_page.input_endTime(str(self.data_generate.creat_time_nextMonth()))
        self.BadEdit_page.click_title()
        self.BadEdit_page.click_submit_button()
        self.assertTrue(int(ad_count)+1 == int(self.BadList_page.get_ad_count()))

    def test_03update_ad(self):
        '''修改广告：取列表第一行，如是视频广告则改为图片广告；如是图片广告改为视频广告'''
        # 后台主页
        self.BsiteMenu_page = BsiteMenu_page.BsiteMenu_page(self.driver)
        self.BsiteMenu_page.click_adIndex()
        # 广告列表页面
        self.BadList_page = BadList_page.BadList_page(self.driver)
        self.BadList_page.click_update_link()
        # 编辑广告页面
        self.BadEdit_page = BadEdit_page.BadEdit_page(self.driver)
        self.BadEdit_page.input_title('ad_update_'+str(self.data_generate.create_randomInt(0, 999)))
        type_value = self.BadEdit_page.get_ad_type()
        print type_value
        if type_value == '0':
            # 视频改为图片
            self.BadEdit_page.select_ad_type('1')
            self.BadEdit_page.input_imgLink(r'http://www.cnblogs.com/helenMemery/')
            self.BadEdit_page.upload_imgFile(gl.img_for_test_path)
        else:
            # 图片改视频
            self.BadEdit_page.select_ad_type('0')
            self.BadEdit_page.input_VideoID('9031868222894357044')
        self.BadEdit_page.click_statue_forbidden()
        self.BadEdit_page.click_submit_button()
        self.assertIn('update', self.BadList_page.get_ad_title())

    def test_04delete_ad(self):
        '''删除广告'''
        # 后台主页
        self.BsiteMenu_page = BsiteMenu_page.BsiteMenu_page(self.driver)
        self.BsiteMenu_page.click_adIndex()
        # 广告列表页面
        self.BadList_page = BadList_page.BadList_page(self.driver)
        ad_count = self.BadList_page.get_ad_count()
        self.BadList_page.click_delete_link()
        self.BadList_page.click_delete_sure()
        self.assertTrue(int(ad_count)-1 == int(self.BadList_page.get_ad_count()))

    def test_05insert_adGroup(self):
        '''新增广告组'''
        # 后台主页
        self.BsiteMenu_page = BsiteMenu_page.BsiteMenu_page(self.driver)
        self.BsiteMenu_page.click_adIndex()
        # 广告列表页面
        self.BadList_page = BadList_page.BadList_page(self.driver)
        self.BadList_page.click_ad_group_index()
        # 广告组管理页面
        self.BadGroupList_page = BadGroupList_page.BadGroupList_page(self.driver)
        adGroup_count = self.BadGroupList_page.get_adGroup_count()
        self.BadGroupList_page.click_add_button()
        # 编辑广告组页面
        self.BadGroupEdit_page = BadGroupEdit_page.BadGroupEdit_page(self.driver)
        self.BadGroupEdit_page.input_name('adGroup_'+str(self.data_generate.create_randomInt(0,999)))
        self.BadGroupEdit_page.input_code(self.data_generate.create_randomLowercase(4))
        self.BadGroupEdit_page.click_submit_button()
        self.assertTrue(int(adGroup_count)+1 == int(self.BadGroupList_page.get_adGroup_count()))

    def test_06update_adGroup(self):
        '''修改广告组'''
        # 后台主页
        self.BsiteMenu_page = BsiteMenu_page.BsiteMenu_page(self.driver)
        self.BsiteMenu_page.click_adIndex()
        # 广告列表页面
        self.BadList_page = BadList_page.BadList_page(self.driver)
        self.BadList_page.click_ad_group_index()
        # 广告组管理页面
        self.BadGroupList_page = BadGroupList_page.BadGroupList_page(self.driver)
        self.BadGroupList_page.click_update_link()
        # 编辑广告组页面
        self.BadGroupEdit_page = BadGroupEdit_page.BadGroupEdit_page(self.driver)
        self.BadGroupEdit_page.input_name('adGroup_update_'+str(self.data_generate.create_randomInt(0,999)))
        self.BadGroupEdit_page.click_submit_button()
        self.assertIn('update', self.BadGroupList_page.get_adGroup_name())

    def test_07delete_adGroup(self):
        '''删除广告组'''
        # 后台主页
        self.BsiteMenu_page = BsiteMenu_page.BsiteMenu_page(self.driver)
        self.BsiteMenu_page.click_adIndex()
        # 广告列表页面
        self.BadList_page = BadList_page.BadList_page(self.driver)
        self.BadList_page.click_ad_group_index()
        # 广告组管理页面
        self.BadGroupList_page = BadGroupList_page.BadGroupList_page(self.driver)
        adGroup_count = self.BadGroupList_page.get_adGroup_count()
        self.BadGroupList_page.click_delete_link()
        self.BadGroupList_page.click_delete_sure_button()
        self.assertTrue(int(adGroup_count)-1 == int(self.BadGroupList_page.get_adGroup_count()))

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        # pass

if __name__ == '__main__':
    unittest.main()
