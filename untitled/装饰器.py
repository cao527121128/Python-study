#coding=utf-8
'''
装饰器：
概述：是一个闭包，把一个函数当作参数返回一个替代版的函数，本质上就是个返回函数的函数

'''
#简单的装饰器1
#在func1默认字符串之前加入一行***  不能直接修改func1
def func1():
    print("Linuxcao is a good man!")

def outer(func):
    def inner():
        print("**********************")
        func1()
    return inner
#f 是 func1的加强版本  是func1的装饰版本 传谁就装饰谁  返回一个替代版的函数
f = outer(func1)
print(type(f))
f()


print("***************")
#复杂的装饰器2
#要求：不能修改say函数本身，但是可以自动过滤年龄为负数的情况
def say(age):
    print("Linuxcao is %d years old" % (age))

#装饰器outer
def outer(func):
    def inner(age):
        if age < 0:
            age = 0
        func(age)
    return inner
say = outer(say)
say(-10)




print("￥￥&&^^^&&&&&")
#复杂的装饰器3---使用@符号
#要求：不能修改say函数本身，但是可以自动过滤年龄为负数的情况

#装饰器outer
def outer(func):
    def inner(age):
        if age < 0:
            age = 0
        func(age)
    return inner

#使用@符号将装饰器应用到函数
#python 2.4开始支持使用@符号
@outer  #相当于 say = outer(say)
def say(age):
    print("Linuxcao is %d years old" % (age))

say(-10)

print("*************")
#更加通用的装饰器-3
def outer(func):
    def inner(*args,**kwargs):
        #添加修改的功能
        print("&&&&&&&&&")
        func(*args,**kwargs)
    return inner
@outer
def say(name,age):
    print("my name is %s,I am %d years old" % (name,age))

say("Linuxcao",18)



