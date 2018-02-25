# coding:utf-8
__author__ = 'Helen'
'''
description:窗口事件共公类
'''


class window_transaction:
    # 获取当前操作窗口句柄
    def window_change(self,all_handles,old_handle):
        for i in all_handles:
            if i != old_handle:
                return i
