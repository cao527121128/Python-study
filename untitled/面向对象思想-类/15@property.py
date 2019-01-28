#coding=utf-8

'''

 @property

'''
class Person(object):
    def __init__(self,age,height):

        #属性直接对外暴露
        self.age = age

        #定义私有属性限制访问，需要自己编写get和set方法外部才能访问
        self.__height = height

    def getHeight(self):
        return self.__height
    def setHeight(self,height):
        if height < 0:
            height = 0
        self.__height = height

    #方法名为受限制的变量去掉双下划线
    #优点：这样外部访问私有属性的时候，可以像不受限的属性一样直接调用，同时里面也加入了限制
    @property
    def height(self):
        return self.__height

    @height.setter  #固定格式：@去掉前面双下划线的私有属性变量.setter
    def height(self,height):
        if height < 0:
            height =0
        self.__height = height


per = Person(18,170)
print(per.age)

#示例1
#属性直接对我暴露
#不安全并且没有经过数据过滤
per.age = -10
print(per.age)


#示例2
#定义私有属性限制访问，需要自己编写get和set方法外部才能访问
per.setHeight(180)
print(per.getHeight())


#示例3
per.height = -10  #相当于调用了 def height(self,height)   设置方法
print(per.height) #相当于调用了 def height(self)   取值方法

#注意：示例3的好吃