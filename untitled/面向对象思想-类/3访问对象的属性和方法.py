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


per = Person()

'''
访问属性
格式：对象名.属性名
赋值：对象名.属性名=新值
'''
per.name = "Linuxcao"
per.age = 32
per.height = 170
per.weight =120
print(per.name,per.age,per.height,per.weight)


'''
访问方法
格式：对象名.方法名（参数列表）
注意：self不需要传

'''
per.openDoor()
per.fillEle()
per.closeDoor()

per.eat("apple")