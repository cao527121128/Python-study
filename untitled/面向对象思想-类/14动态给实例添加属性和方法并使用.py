#coding=utf-8

from types import MethodType

#创建一个空类
class Person(object):
    __slots__ = ("name","age","speek")


per = Person()

#动态添加属性  这体现了动态语言的特点 灵活
per.name = "Tom"
print(per.name)


#动态添加方法
def say(self):
    print("my name is "+ self.name)
#类比偏函数
#把say函数的参数固定为per传给self,形成一个新的函数，返回给speek  这样调用speek就不需要带参数
per.speek =MethodType(say,per)
per.speek()


#思考：如果我们想要限制实例的属性如何解决？
#例如：只允许给对象添加name age speek属性呢？
#解决办法：定义类的时候，定义一个特殊的属性(__slots__)  可以限制动态添加的属性
per.height = 170
print(per.height)