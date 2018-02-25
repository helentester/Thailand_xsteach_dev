# coding:utf-8
__author__ = 'Helen'
'''
description:接口测试
'''
import requests,unittest,ddt
from src.common.excel_data import excel
# 测试数据
excel_data = excel()
test_data = excel_data.get_list("interface_data")


@ddt.ddt
class test_Interface(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print u'开始测试'

    @ddt.data(*test_data)
    def test_interface(self,test_data):
        print u'接口名称：'+test_data['interface_name']
        try:
            if test_data['request_type']=='get':
                r = requests.get(url=test_data['URL'],params=test_data['parameters'])
            elif test_data['request_type']=='post':
                r = requests.post(url=test_data['URL'],data=test_data['parameters'])
            print r.status_code
            assert r.status_code == 200
        except requests.HTTPError,e:
            raise e

    @classmethod
    def tearDownClass(cls):
        print u'结束测试'