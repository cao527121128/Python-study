#coding=utf-8

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
        print("eat " + food)
    def openDoor(self):
        print("open door")
    def fillEle(self):
        print("fill Ele")
    def closeDoor(self):
        print("close door")
    def __init__(self,name,age,height,weight):
        print("这里是init")
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        pass


'''
构造函数：__init__() 在使用类创建对象的时候自动调用
注意：如果不显示的写出构造函数，默认会自动添加一个空的init构造函数
self: 代表当前正在创建的对象

'''
per = Person("hanmeimei",20,170,55)
print(per.name,per.age,per.height,per.weight)
