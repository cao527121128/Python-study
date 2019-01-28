# coding=utf-8
'''
不定长参数：
概述：能处理比定义时更多的参数

'''


# 加了 * 的变量会存放所有未命名的变量参数，如果在函数调用时没有指定参数，它就是一个空元组
def func(name, *args):
    print(name)
    print(type(args))
    for x in args:
        print(x)


func("Linuxcao", "nice", "good", "handsome")


# 例子1
def mySum(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


res = mySum(1, 2, 3, 4, 5)
print(res)


# 例子2
# ** 代表键值对的参数字典  和*代表的意义类似
def func2(**kwargs):
    print(kwargs)
    print(type(kwargs))


func2(x=1, y=2, z=3)

print("************")

# 例子3
# 可以接收任意参数
def func3(*args, **kwargs):
    pass  # 代表空语句
    for x in args:
        print(x)
    print(kwargs)
func3(x=1,y=2,z=3)
func3(1,2,3,4)
