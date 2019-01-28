#coding=utf-8
import datetime
import time

'''
datetime 是基于time进行封装了一次，datetime模块的接口更加直观
datetime模块中的类：
datetime  同时有时间和日期
timedelta  主要用于计算时间的跨度
tzinfo    时区相关
time      只关注时间
date    只关注日期

'''


#获取当前时间
d1 = datetime.datetime.now()
print(d1)
print(type(d1))

#获取指定时间
d2 = datetime.datetime(1986,11,18,10,11)
print(d2)

#将时间转成时间字符串
d1 = datetime.datetime.now()
d3 = d1.strftime("%Y-%m-%d %X")
print(d3)

#当前时间减去过去某一个时间
d5 = datetime.datetime(1986,11,18,10,11)
d6 = datetime.datetime.now()
d7 = d6 - d5
print(d7)
#间隔的天数
print(d7.days)


#获取昨天日期字符串：
yesterday = (datetime.datetime.now()+datetime.timedelta(days=-1)).strftime("%Y-%m-%d")
print(yesterday)