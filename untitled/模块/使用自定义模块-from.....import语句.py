#coding=utf-8
'''
from.....import语句
作用：从模块中导入一个指定的部分（函数方法）到当前命名空间
格式：from module import name1[,name2,name3....namen]

'''
# 相当于把sayGood sayNice函数定义在这个位置
from Linuxcao import sayGood,sayNice
'''

#弊端：程序里面的函数可以将模块中的同名函数覆盖
def sayGood():
    print("*********")
'''
#调用
sayGood()
#Linuxcao.sayGood()
sayNice()
#sayHandsome()  #没有引入handsome方法

