#coding=utf-8
# 需求：编写一个函数，给函数一个字符串和一个年龄，在函数内部打印出来

#形参（形式参数），定义函数时小括号内的变量，本质是变量
#参数必须按顺序传递，个数目前要对应
def myPrint(str,age):
    print(str,age)

#实参（实际参数），调用函数是传递给函数的实际数值，本质是值
myPrint("Linuxcao is a good man!",18)