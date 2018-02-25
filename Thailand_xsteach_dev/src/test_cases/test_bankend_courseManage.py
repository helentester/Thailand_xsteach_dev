# coding:utf-8
__author__ = 'Helen'
'''
description:测试1、课程管理（VIP课程+公开课程）；2、课程分类管理
'''
import unittest,time
from config import globalparameter as gl
from src.common.data_generating import data_generating
import public_module
from src.backendPages.BsiteMenu_page import BsiteMenu_page
from src.backendPages.BcourseList_page import BcourseList_page
from src.backendPages.BcourseEdit_page import BcourseEdit_page
from src.backendPages.BvideoList_page import BvideoList_page
from src.backendPages.BvideoEdit_page import BvideoEdit_page
from src.backendPages.BcourseStudentList_page import BcourseStudentList
from src.backendPages.BcourseStudentEdit_page import BcourseStudentEdit_page


class test_bankend_courseManage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.PM = public_module.public_module()
        cls.data_generate = data_generating()
        # 登录
        cls.driver = cls.PM.Blogin()

    def test_01insertVIPcourse(self):
        '''新增VIP课'''
        # 后台主页
        self.BsiteMenu_page = BsiteMenu_page(self.driver)
        self.BsiteMenu_page.click_courseIndex()

        # 课程列表页面
        self.BcourseList_page = BcourseList_page(self.driver)
        course_count = self.BcourseList_page.get_course_count()
        self.BcourseList_page.click_createVIPCourse_button()

        # 新增VIP课程页面
        self.BcourseEdit_page = BcourseEdit_page(self.driver)
        course_name = 'VIP_course'+ str(self.data_generate.create_randomInt(0, 999))
        course_price = str(self.data_generate.create_randomFloat(0, 9999, 2))
        self.BcourseEdit_page.input_course_name(course_name)
        self.BcourseEdit_page.click_course_category()
        self.BcourseEdit_page.click_course_teacher()
        self.BcourseEdit_page.click_course_term()
        self.BcourseEdit_page.upload_littleImg(gl.img_for_test_path)
        self.BcourseEdit_page.upload_bigImg(gl.img_for_test_path)
        self.BcourseEdit_page.input_course_price(course_price)
        self.BcourseEdit_page.input_course_intro('this course insert by selenium ,for auto test')
        self.BcourseEdit_page.click_submit_button()
        self.assertTrue(int(course_count)+1 == int(self.BcourseList_page.get_course_count()))

    def test_02insertVIPVideo(self):
        '''新增VIP课程中的视频'''
        # 后台主页
        self.BsiteMenu_page = BsiteMenu_page(self.driver)
        self.BsiteMenu_page.click_courseIndex()
        # 课程列表页面
        self.BcourseList_page = BcourseList_page(self.driver)
        self.BcourseList_page.click_video_link()
        # 视频列表页面
        self.BvideoList_page = BvideoList_page(self.driver)
        self.BvideoList_page.click_insert_button()
        # 视频编辑页面
        self.BvideoEdit_page = BvideoEdit_page(self.driver)
        classTheme = 'VIP_video'+str(self.data_generate.create_randomInt(1,999))
        self.BvideoEdit_page.input_classTheme(classTheme)
        self.BvideoEdit_page.input_videoID('9031868222894357044')
        self.BvideoEdit_page.click_videoLength()
        self.BvideoEdit_page.click_submitButton()
        # 回到视频列表页面断言
        self.assertEqual(classTheme, self.BvideoList_page.get_videoName_at_firstLine())

    def test_03insertCourseStudent(self):
        '''新增VIP课程中的课程学员'''
        # 后台主页
        self.BsiteMenu_page = BsiteMenu_page(self.driver)
        self.BsiteMenu_page.click_courseIndex()
        # 课程列表页面
        self.BcourseList_page = BcourseList_page(self.driver)
        self.BcourseList_page.click_studentListLink_at_firstList()
        # 课程学员列表页面
        self.BcourseStudentList_page = BcourseStudentList(self.driver)
        self.BcourseStudentList_page.click_addStudent_button()
        # 添加课程学员页面
        self.BcourseStudentEdit_page = BcourseStudentEdit_page(self.driver)
        self.BcourseStudentEdit_page.input_studentUID('28') # 现在都以该学员添加
        self.BcourseStudentEdit_page.click_submit_button()
        self.assertEqual('28',self.BcourseStudentList_page.get_studentUID_at_firstLine())

    def test_04insertOpenCourse(self):
        '''新增公开课'''
        # 后台主页
        self.BsiteMenu_page = BsiteMenu_page(self.driver)
        self.BsiteMenu_page.click_courseIndex()
        # 课程列表页面
        self.BcourseList_page = BcourseList_page(self.driver)
        self.BcourseList_page.click_openCourseList()
        course_count = self.BcourseList_page.get_course_count()
        self.BcourseList_page.click_createOpenCourse_button()
        # 新增公开课页面
        self.BcourseEdit_page = BcourseEdit_page(self.driver)
        course_name = 'OpenCourse'+ str(self.data_generate.create_randomInt(0, 999))
        self.BcourseEdit_page.input_course_name(course_name)
        self.BcourseEdit_page.click_course_category()
        self.BcourseEdit_page.click_course_teacher()
        self.BcourseEdit_page.upload_littleImg(gl.img_for_test_path)
        self.BcourseEdit_page.upload_bigImg(gl.img_for_test_path)
        self.BcourseEdit_page.input_course_intro('this course insert by selenium ,for auto test')
        self.BcourseEdit_page.click_submit_button()
        self.BcourseList_page.click_openCourseList()
        self.assertTrue(int(course_count)+1 == int(self.BcourseList_page.get_course_count()))

    def test_05insertOpenVideo(self):
        '''新增公开课的视频'''
        # 后台主页
        self.BsiteMenu_page = BsiteMenu_page(self.driver)
        self.BsiteMenu_page.click_courseIndex()
        # 课程列表页面
        self.BcourseList_page = BcourseList_page(self.driver)
        self.BcourseList_page.click_openCourseList()
        self.BcourseList_page.click_video_link()
        # 视频列表页面
        self.BvideoList_page = BvideoList_page(self.driver)
        self.BvideoList_page.click_insert_button()
        # 视频编辑页面
        self.BvideoEdit_page = BvideoEdit_page(self.driver)
        classTheme = 'OpenVideo'+str(self.data_generate.create_randomInt(1,999))
        self.BvideoEdit_page.input_classTheme(classTheme)
        self.BvideoEdit_page.input_videoID('9031868222894357044')
        self.BvideoEdit_page.click_videoLength()
        self.BvideoEdit_page.click_submitButton()
        # 回到视频列表页面断言
        self.assertEqual(classTheme, self.BvideoList_page.get_videoName_at_firstLine())

    def test_06updateVIPcourse(self):
        '''查询+修改VIP课程'''
        # 后台主页
        self.BsiteMenu_page = BsiteMenu_page(self.driver)
        self.BsiteMenu_page.click_courseIndex()
        # 课程列表页面
        self.BcourseList_page = BcourseList_page(self.driver)
        self.BcourseList_page.select_search_status(u'上架')
        self.BcourseList_page.click_search_button()
        self.BcourseList_page.click_update_link()
        # 编辑课程页面
        self.BcourseEdit_page = BcourseEdit_page(self.driver)
        course_name = 'VipCourse_update_' + str(self.data_generate.create_randomInt(0,999))
        self.BcourseEdit_page.input_course_name(course_name)
        self.BcourseEdit_page.click_statue_notSell()
        self.BcourseEdit_page.click_submit_button()
        # 回到课程列表断言：课程状态更改为下架
        self.BcourseList_page.input_search_keyword(course_name)
        self.BcourseList_page.click_search_button()
        self.assertEqual(u'下架', self.BcourseList_page.get_course_statue())

    def test_07updateOpenCourse(self):
        '''查询+修改公开课'''
        # 后台主页
        self.BsiteMenu_page = BsiteMenu_page(self.driver)
        self.BsiteMenu_page.click_courseIndex()
        # 课程列表页面
        self.BcourseList_page = BcourseList_page(self.driver)
        self.BcourseList_page.click_openCourseList()
        self.BcourseList_page.select_search_status(u'上架')
        self.BcourseList_page.click_search_button()
        time.sleep(2)
        self.BcourseList_page.click_update_link()
        # 编辑课程页面
        self.BcourseEdit_page = BcourseEdit_page(self.driver)
        self.BcourseEdit_page.input_course_name('openCourse_update_'+str(self.data_generate.create_randomInt(0,999)))
        self.BcourseEdit_page.click_statue_notSell()
        self.BcourseEdit_page.click_submit_button()
        self.BcourseList_page.click_openCourseList()
        self.assertEqual(u'下架', self.BcourseList_page.get_course_statue())

    def test_08updateVIPVideo(self):
        '''修改VIP课程的视频:修改课时主题和试学状态'''
        # 后台主页
        self.BsiteMenu_page = BsiteMenu_page(self.driver)
        self.BsiteMenu_page.click_courseIndex()
        # 课程列表页面
        self.BcourseList_page = BcourseList_page(self.driver)
        self.BcourseList_page.click_video_link()
        # 视频列表页面
        self.BvideoList_page = BvideoList_page(self.driver)
        video_freeStatue = self.BvideoList_page.get_free_statue()
        print video_freeStatue
        self.BvideoList_page.click_update_VIPvideo_link()
        # 视频编辑页面
        self.BvideoEdit_page = BvideoEdit_page(self.driver)
        self.BvideoEdit_page.input_classTheme('video_update_'+str(self.data_generate.create_randomInt(0,999)))
        self.BvideoEdit_page.click_free_statue()
        self.BvideoEdit_page.click_submitButton()
        self.assertNotEqual(video_freeStatue, self.BvideoList_page.get_free_statue())

    def test_updateCourseStudent(self):
        '''修改VIP课程的学员'''
        # 后台主页
        self.BsiteMenu_page = BsiteMenu_page(self.driver)
        self.BsiteMenu_page.click_courseIndex()
        # 课程列表页面
        self.BcourseList_page = BcourseList_page(self.driver)
        self.BcourseList_page.click_studentListLink_at_firstList()
        # 学员列表页面
        self.BcourseStudentList_page = BcourseStudentList(self.driver)
        studentUID = self.BcourseStudentList_page.get_studentUID_at_firstLine()
        self.BcourseStudentList_page.click_update_button()
        # 编辑学员页面
        self.BcourseStudentEdit_page = BcourseStudentEdit_page(self.driver)
        # 因为测试按顺序执行，插入的时候用的UID＝28，修改的时候改27
        if studentUID=='28':
            new_studentUID = '27'
        else:
            new_studentUID = '28'
        self.BcourseStudentEdit_page.input_studentUID(new_studentUID)
        self.BcourseStudentEdit_page.click_submit_button()
        self.assertEqual(new_studentUID, self.BcourseStudentList_page.get_studentUID_at_firstLine())

    def test_09updateOpenVideo(self):
        '''修改公开课的视频'''
        # 后台主页
        self.BsiteMenu_page = BsiteMenu_page(self.driver)
        self.BsiteMenu_page.click_courseIndex()
        # 课程列表页面
        self.BcourseList_page = BcourseList_page(self.driver)
        self.BcourseList_page.click_openCourseList()
        self.BcourseList_page.click_video_link()
        # 视频列表页面
        self.BvideoList_page = BvideoList_page(self.driver)
        self.BvideoList_page.click_update_openVideo_link()
        # 编辑视频列表页面
        self.BvideoEdit_page = BvideoEdit_page(self.driver)
        open_classTheme = 'openVideo_update_'+str(self.data_generate.create_randomInt(0,999))
        self.BvideoEdit_page.input_classTheme(open_classTheme)
        self.BvideoEdit_page.click_submitButton()
        self.assertEqual(open_classTheme,self.BvideoList_page.get_videoName_at_firstLine())

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        # pass

if __name__ == '__main__':
    unittest.main()



