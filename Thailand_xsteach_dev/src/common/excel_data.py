# coding:utf-8
__author__ = 'Helen'
'''
description:读取excel文件
'''
import xlrd
from src.common import log
from config.globalparameter import test_data_path


class excel:
    def __init__(self):
        self.mylog = log.log()

    def open_excel(self,file):
        u'''读取excel文件'''
        try:
            data = xlrd.open_workbook(file)
            return data
        except Exception, e:
            self.mylog.error(u"打开excel文件失败")

    def excel_table(self,file, sheetName):
        u'''装载list'''
        data = self.open_excel(file)
        # 通过工作表名称，获取到一个工作表
        table = data.sheet_by_name(sheetName)
        # 获取行数
        Trows = table.nrows
        # 获取 第一行数据
        Tcolnames = table.row_values(0)
        lister = []
        for rownumber in range(1,Trows):
            row = table.row_values(rownumber)
            if row:
                app = {}
                for i in range(len(Tcolnames)):
                    app[Tcolnames[i]] = row[i]
                lister.append(app)
        return lister

    def get_list(self,sheetname):
        try:
            data_list = self.excel_table(test_data_path, sheetname)
            assert len(data_list)>=0,u'excel标签页:'+sheetname+u'为空'
            return data_list
        except Exception as e:
            self.mylog.error(u'excel标签页:'+sheetname+u'为空')
            raise e
