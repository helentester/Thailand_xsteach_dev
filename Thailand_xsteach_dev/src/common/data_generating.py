# coding:utf-8
__author__ = 'Helen'
'''
description:生成各类数据
'''
import random,datetime


class data_generating():
    def __call__(self, *args, **kwargs):
        pass

    def create_PhoneNo(self):
        '''生成电话号码'''
        prelist=["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150","151","152","153","155","156","157","158","159","186","187","188"]
        return random.choice(prelist)+"".join(random.choice("0123456789") for i in range(8))

    def create_randomInt(self, lower, upper):
        '''生成随机整数'''
        return random.randint(lower,upper)

    def create_randomFloat(self, lower, upper, point_length):
        '''生成小数点后point_length位的浮点数'''
        return round(random.uniform(lower, upper), point_length)

    def create_randomLowercase(self,letters_len):
        '''生成随机字母：小写'''
        return "".join(random.choice("abcdefghijklmnopqrstuvwxyz") for i in range(letters_len))


    # 返回时间：当天
    def create_time_today(self):
        return datetime.date.today()

    # 返回时间：一个月后的时间
    def creat_time_nextMonth(self):
        return datetime.date.today() + datetime.timedelta(days=31)
