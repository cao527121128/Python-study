#coding=utf-8
import  functools
'''
偏函数：
概述：
把一个参数固定住，形成一个新的函数

'''

#默认字符串转成整型，以2进制存放 以十进制方式输出
print(int("1010",base=2))

#要求：不传base=2

#手动编写偏函数-1
def int2(str,base=2):
    return int(str,base)
print(int2("1010"))


#直接使用functools模块生成偏函数-2
int3 = functools.partial(int,base = 2)  #把int函数的base参数固定为2,形成一个新的函数，返回给int3
print(int3("1010"))