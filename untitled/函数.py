#coding=utf-8
'''
函数：
本质: 功能的封装

'''

'''
1、函数的格式：
def 函数名（参数列表）:
    语句
    return 表达式
    

def:函数代码块以def关键字开始
函数名：遵循标识符规则
参数列表（参数1，参数2，参数3.....参数n）：任何传入函数的参数和变量都必须放在圆括号内，用逗号隔开。
函数从函数的调用者那里获取信息
冒号：函数内容（封装的功能）以冒号开始，并且缩进
语句：函数封装的功能
return:一般用于结束函数，并返回信息给函数的调用者
表达式：即为要返回给函数的调用者的信息

注意：最后的return 表达式，可以不写，相当于return None

2、函数的调用：
格式：
函数名（参数列表）
函数调用的本质：实参给形参赋值的过程

'''

#定义一个无参数无返回值的函数
def myPrint():
    print("Linuxcao is a good man!")
    print("Linuxcao is a nice man!")
    print("Linuxcao is a handsome man!")
    return None

#调用
myPrint()
myPrint()
