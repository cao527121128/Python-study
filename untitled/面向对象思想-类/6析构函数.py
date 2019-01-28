#coding=utf-8

'''
析构函数作用：释放对象，减少内存占用
析构函数格式：
def __del__(self):
    pass


1、程序结束会自动释放对象
2、手动释放对象
del 对象名

3、在函数里面定义的对象，在函数结束的时候会自动释放

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
        print("这里是析构函数")

per = Person("Hanmeimei",20,165,50)

#1 手动释放对象
del per


#2 在函数里面定义的对象，在函数结束的时候会自动释放，这样可以减少内存空间的浪费，函数结束，就自动释放对象内存
def func():
    per2 = Person("Tom",20,170,60)
func()


while 1:
    pass
