#coding=utf-8
'''
重写：将函数定义重写一遍
__str__():在调用print打印对象的时候自动调用，是给用户用的，是一种描述对象的方法

__repr__():是给机器用的，在python解释器里面直接敲对象名再回车后自动调用的方法

注意：在没有str时，且有repr时，repr相当于str

应用场景：当一个对象的属性比较多，并且需求打印出来，我们就可以重写__str__()函数，
使用__str__()函数打印出来，简化代码

'''

class Person(object):
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
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        pass
    def __del__(self):
        pass
        #print("这里是析构函数")
    def __str__(self):
        return "%s--%d--%d--%d" %(self.name,self.age,self.height,self.weight)

per = Person("Hanmeimei",20,165,50)
#print(per.name,per.age,per.height,per.weight)
print(per)  #打印对象相当print(per.__str__())

