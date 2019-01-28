#coding=utf-8
from collections import Iterable
from collections import Iterator
'''
可迭代对象：可以直接用于for循环的对象统称为可迭代对象（Iterable）
可以使用isinstance(object,Iterable)去判断一个对象是否是可迭代对象(Iterable)

可以直接作用于for的数据类型一般分为两种：
1、集合数据类型：如list、tuple、dict、字符串、set
2、是generactor,包括生成器和带yield generactor function

'''
#判断是否为可迭代对象？
print(isinstance([],Iterable))  #判断列表是否为可迭代对象
print(isinstance({},Iterable))
print(isinstance((),Iterable))
print(isinstance("Linuxcao",Iterable))
print(isinstance(1,Iterable))
print(isinstance((x for x in range(10)),Iterable))


'''
迭代器:不但可以作用于for循环，还可以被next() 函数不断调用并返回下一个值
直到最好抛出一个StopIteration错误表示无法继续返回下一个值为止。
概述：
可以被next()函数调用并不断返回下一个值的对象称为迭代器（Iterator.
可以使用isinstance(object,Iterator)去判断一个对象是否是迭代器对象(Iterator)
'''
print("****************")
#判断是否为迭代器对象Iterator？
print(isinstance([],Iterator))  #判断列表是否为迭代器对象Iterator
print(isinstance({},Iterator))
print(isinstance((),Iterator))
print(isinstance("Linuxcao",Iterator))
print(isinstance(1,Iterator))
print(isinstance((x for x in range(10)),Iterator))

#迭代器的使用
l = (x for x in range(5))
print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))
#print(next(l))  #抛出异常StopIteration

print("************")
#列表转成Iterator对象
a = iter([1,2,3,4,5])
print(next(a))
print(next(a))

#元组转成Iterator对象
a = iter((1,2,3,4,5))
print(next(a))
print(next(a))


#字符串转成Iterator对象
a = iter("Linuxcao")
print(next(a))
print(next(a))

#判断是否为迭代器对象Iterator？
print(isinstance(iter([]),Iterator))  #判断列表是否为迭代器对象Iterator
print(isinstance(iter(()),Iterator))
print(isinstance(iter({}),Iterator))
print(isinstance(iter("Linuxcao"),Iterator))

#使用案例
print("**************")
#输入字符串，直到输入了end才结束
endstr = "end"
str = ""
for line in iter(raw_input,endstr):
    str += line + '\n'
print(str)






