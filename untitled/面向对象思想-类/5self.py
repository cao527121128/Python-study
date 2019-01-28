#coding=utf-8
'''
self 代表类的实例，而非类
哪个对象调用方法，那么该方法中的self就代表那个对象
self.__class__  代表类名

'''

class Person(object):
    #定义方法(也即是定义函数)
    #注意：方法的参数必须以self为第一个参数
    #self代表类的实例（某一个对象）
    def run(self):
        print("run")
        #self.__class__  代表类名 可以等同于p=Persion("lilei",20,170,130)  创建Person对象
        print(self.__class__)
        p = self.__class__("lilei",20,170,130)
        print(p)
    def eat(self,food):
        print("eat " + food)
    def openDoor(self):
        print("open door")
    def fillEle(self):
        print("fill Ele")
    def closeDoor(self):
        print("close door")

    def say(self):
        print("Hello! my name is  %s, I am %d years old" %(self.name,self.age))

    #self不是关键字，换成其他的字符也是可以，但是约定俗成都是使用self字符
    def play(a):
        print("play " + a.name)

    def __init__(self,name,age,height,weight):
        #print("这里是init")
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        pass

    
per1 = Person("hanmeimei",20,170,55)
per1.say()


per2 = Person("Tom",22,175,70)
per2.say()

per2.play()
per2.run()
