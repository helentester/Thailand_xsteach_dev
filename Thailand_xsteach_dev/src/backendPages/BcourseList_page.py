# coding:utf-8
__author__ = 'Helen'
'''
description:课程列表页面
'''
from src.common.Base_Page import BasePage
from selenium.webdriver.common.by import By


class BcourseList_page(BasePage):
    # 定位器
    search_keyword_loc = (By.CSS_SELECTOR, "#keyword")  # 查询－课程名称关键词
    search_status_loc = (By.CSS_SELECTOR, ".form-wrap>select[name='status']")   # 查询－状态下拉框
    search_button_loc = (By.CSS_SELECTOR, ".btn.btn-primary.ml10")  # 查询按钮

    createVIPCourse_button_loc = (By.CSS_SELECTOR, ".btn.btn-default.btn-sm.right[href='/course/create?type=V']")   # 新增VIP课程按钮
    createOpenCourse_button_loc = (By.CSS_SELECTOR, ".btn.btn-default.btn-sm.right[href='/course/create?type=O']")  # 新增公开课按钮
    courseList_loc = (By.CSS_SELECTOR, ".nav.nav-tabs>li>a[href='/course/index?type=O']")   # 公开课标签页
    course_count_loc = (By.CSS_SELECTOR, ".summary>b:nth-child(2)")     # 课程记录数

    courseName_at_firstList_loc = (By.XPATH, ".//*[@id='w0']/table/tbody/tr[1]/td[1]")  # 课程列表中第一行第一列表(课程名称)
    course_statue_loc = (By.XPATH, ".//*[@id='w0']/table/tbody/tr[1]/td[4]")    # 课程列表中第一行第4列（状态）
    update_link_loc = (By.XPATH, ".//*[@id='w0']/table/tbody/tr[1]/td[5]/a[1]") # 课程列表中第一行最后一例(编辑链接)
    video_link_loc = (By.XPATH, ".//*[@id='w0']/table/tbody/tr[1]/td[5]/a[2]")  # 课程列表中第一行最后一例(视频录播链接)
    studentListLink_at_firstLis_loc = (By.XPATH, ".//*[@id='w0']/table/tbody/tr[1]/td[5]/a[3]")  # 课程列表中第一行最后一例(课程学员链接）

    # 输入课程名称关键词
    def input_search_keyword(self, course_name):
        self.send_keys(course_name, *self.search_keyword_loc)

    # 选择课程状态
    def select_search_status(self, course_status):
        self.select_value('By_text', course_status, *self.search_status_loc)

    # 点击查询按钮
    def click_search_button(self):
        self.find_element(*self.search_button_loc).click()

    # 点击新增VIP课程按钮
    def click_createVIPCourse_button(self):
        self.find_element(*self.createVIPCourse_button_loc).click()

    # 获取第一行的课程名称
    def get_course_name(self):
        return self.find_element(*self.courseName_at_firstList_loc).text

    # 获取第一行的课程状态
    def get_course_statue(self):
        return self.find_element(*self.course_statue_loc).text

    # 点击第一行的“编辑”链接
    def click_update_link(self):
        self.find_element(*self.update_link_loc).click()

    # 点击第一行的“视频录播”按钮
    def click_video_link(self):
        self.find_element(*self.video_link_loc).click()

    # 点击第一行的“课程学员”链接
    def click_studentListLink_at_firstList(self):
        self.find_element(*self.studentListLink_at_firstLis_loc).click()

    # 点击新增公开课按钮
    def click_createOpenCourse_button(self):
        self.find_element(*self.createOpenCourse_button_loc).click()

    # 点击打开公开课标签页
    def click_openCourseList(self):
        self.find_element(*self.courseList_loc).click()

    # 获取课程记录数
    def get_course_count(self):
        return self.find_element(*self.course_count_loc).text
