#coding=utf-8
'''
创建类
类：一种数据类型，本身并不占用内存，与number、string、boolean类似
用类创建实例化对象也即是变量时候，该变量会占用内存空间

格式：
class 类名（父类列表）:
    属性
    行为


'''

#object:基类也叫超类，所有类的父类，一般没有合适的父类就写object
class Person(object):
    #定义属性
    name = ""
    age = 0
    height = 0
    weight = 0
    #定义方法(也即是定义函数)
    #注意：方法的参数必须以self为第一个参数
    #self代表类的实例（某一个对象）
    def run(self):
        print("run")
    def eat(self,food):
        print("eat" + food)

