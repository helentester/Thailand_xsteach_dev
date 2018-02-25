# coding:utf-8
__author__ = 'Helen'
'''
description:封装页面公用方法
2017/05/24:去掉日志功能，直接抛异常
'''
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from config.globalparameter import img_path
from selenium.webdriver.common.by import By


class BasePage(object):
    def __init__(self, selenium_driver):
        self.driver = selenium_driver
        # self.url = base_url
        # self.title = page_title
        # self.mylog = log.log()

    #   打开页面,并校验链接是否加载正确
    def _open(self, url, page_title):
        try:
            self.driver.get(url)
            self.driver.maximize_window()
#           通过断言输入的title是否在当前title中
            assert page_title in self.driver.title, u'打开页面失败：%s' % url
        except Exception as e:
            raise e
            # self.mylog.error(u'未能正确打开页面:'+url)

    #   重写find_element方法，增加定位元素的健壮性
    def find_element(self, *loc):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except Exception as e:
            raise e
            # self.mylog.error(u'找不到元素:'+str(loc))

    #   重写send_keys方法
    def send_keys(self, value,*loc):
        try:
            self.find_element(*loc).clear()
            self.find_element(*loc).send_keys(value)
        except AttributeError as a:
            raise a
            # self.mylog.error(u'输入失败,loc='+str(loc)+u';value='+value)

    #   下拉框select元素操作
    def select_value(self,select_way,select_value,*loc):
        try:
            s = self.find_element(*loc)
            print s.get_attribute("value")
            print loc
            if select_way == 'By_index':
                Select(s).select_by_index(int(select_value))
            elif select_way == 'By_value':
                Select(s).select_by_value(select_value)
            elif select_way == 'By_text':
                Select(s).select_by_visible_text(select_value)
            s.click()
        except Exception as e:
            raise e

    # 从table表格中取值：从一列中找到目标数据
    def get_text_from_table(self, tr_index, target_value, *loc):
        table = self.find_element(*loc)
        row = table.find_elements(By.TAG_NAME, "tr")
        for i in row:
            cols = i.find_elements(By.TAG_NAME, "td")
            if len(cols):
                if cols[tr_index].text == target_value:
                    return cols

    #   截图
    def img_screenshot(self, img_name):
        try:
            self.driver.get_screenshot_as_file(img_path+img_name+'.png')
        except Exception as e:
            raise e
            # self.mylog.error(u'截图失败：'+img_name)

    #   执行JS
    def execute_JS(self, js):
        try:
            self.driver.execute_script(js)
        except Exception as e:
            raise e
