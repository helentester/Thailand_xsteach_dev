# coding:utf-8
__author__ = 'Helen'
'''
description:遍历Table表格
'''
import requests

# 业绩入库，userid=学员ID；salesId=班主任UID
print requests.get(url="http://spring.dev.xsteach.com/api/test/order?userId=8397527&salesId=8397520&orderNo=XS-170616-452059&amount=2000&orderId=19336")
# print requests.get(url="http://spring.dev.xsteach.com/personal/performance").text