#coding=utf-8
'''
默认参数：
调用函数是，如果没有传递参数，则使用默认参数
'''

#如果要使用默认参数，最后是将默认参数放在最后一个
def myPrint(str ,age = 18):
    print(str,age)

myPrint("Linuxcao is a good man!")