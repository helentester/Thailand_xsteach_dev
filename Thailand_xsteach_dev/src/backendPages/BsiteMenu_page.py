# coding:utf-8
__author__ = 'Helen'
'''
description:后台左则目录链接
'''
from src.common.Base_Page import BasePage
from selenium.webdriver.common.by import By


class BsiteMenu_page(BasePage):
    # 定位器
    courseIndex_loc = (By.CSS_SELECTOR, ".site-menu>li>a[href='/course/index']")    # 课程管理
    orderIndex_loc = (By.CSS_SELECTOR, ".site-menu>li>a[href='/order/index']")  # 订单管理
    studentIndes_loc = (By.CSS_SELECTOR, ".site-menu>li>a[href='/users/index']")    # 学员管理
    adIndex_loc = (By.CSS_SELECTOR, ".site-menu>li>a[href='/ad/index']")    # 广告管理
    teacherIndex_loc = (By.CSS_SELECTOR, ".site-menu>li>a[href='/teacher/index']")  # 老师管理
    userIndex_loc = (By.CSS_SELECTOR, ".site-menu>li>a[href='/admin/index']")   # 用户管理
    departmentIndex_loc = (By.CSS_SELECTOR, ".site-menu>li>a[href='/department/index']")     # 部门管理
    language_zhCN_loc = (By.CSS_SELECTOR, ".main-inner>ul>li>a[href='/default/lang?language=zh-CN']")   # 语言，中文版

    # 点击课程目录进入课程列表页面（默认VIP）
    def click_courseIndex(self):
        self.find_element(*self.courseIndex_loc).click()

    # 点击进入订单管理页面
    def click_orderIndex(self):
        self.find_element(*self.orderIndex_loc).click()

    # 点击学员管理
    def click_studentIndex(self):
        self.find_element(*self.studentIndes_loc).click()

    # 点击进入广告管理页面
    def click_adIndex(self):
        self.find_element(*self.adIndex_loc).click()

    # 点击进入老师管理页面
    def click_teacherIndex(self):
        self.find_element(*self.teacherIndex_loc).click()

    # 点击进入用户管理页面
    def click_userIndex(self):
        self.find_element(*self.userIndex_loc).click()

    # 点击进入部门管理页面
    def click_departmentIndex(self):
        self.find_element(*self.departmentIndex_loc).click()

    # 点击语言切换按钮：中文版
    def click_language_zhCN(self):
        self.find_element(*self.language_zhCN_loc).click()
