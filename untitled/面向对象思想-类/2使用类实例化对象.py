#coding=utf-8
'''
实例化对象
格式：对象名=类名（参数列表）
注意：没有参数列表，小括号也不能省掉


'''



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
    def openDoor(self):
        print("open door")
    def fillEle(self):
        print("fill Ele")
    def closeDoor(self):
        print("close door")

#实例化一个对象
per1 = Person()
print(per1) #打印Person对象的内存地址
print(type(per1))

per2 = Person()
print(per2)
print(type(per2))