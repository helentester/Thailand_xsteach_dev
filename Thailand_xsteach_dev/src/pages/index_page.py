# coding:utf-8
__author__ = 'Helen'
'''
description:首页
'''
from config import globalparameter as gl
from src.common.Base_Page import BasePage
from selenium.webdriver.common.by import By


class index_page(BasePage):
    # 定位器
    login_link_loc = (By.CSS_SELECTOR, '.loginBox.ml30.fr>li>a:nth-child(1)')
    user_icon_loc = (By.CLASS_NAME, 'userPic')
    classes_link_loc = (By.XPATH, 'html/body/header/div/div[1]/ul/li[2]/a')

    # 打开页面
    def open(self):
        self._open(gl.URL_base,gl.pro_title)

    # 点击登录链接
    def click_login_linck(self):
        self.find_element(*self.login_link_loc).click()

    # 用户头像图片
    def user_icon(self):
        return self.find_element(*self.user_icon_loc).is_displayed()

    # 点击课程链接
    def click_classes_link(self):
        self.find_element(*self.classes_link_loc).click()
