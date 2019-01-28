#coding=utf-8
'''
lambda函数的语法只包含一个语句，
格式：
lambda arg1,arg2,.....argn:expression
'''

#实例
# 冒号:之前的num1 num2表示它们是这个函数的参数。
# 匿名函数不需要return来返回值，表达式本身结果就是返回值。
sum = lambda num1,num2:num1 + num2
res = sum(1,2)
print(res)