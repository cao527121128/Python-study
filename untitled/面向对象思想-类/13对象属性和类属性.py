#coding=utf-8
'''
对象属性的优先级是高于类属性


'''

class  Person(object):
    #这里的属性实际上是类属性(使用类名来调用)
    name = "person"
    def __init__(self,name):
        #对象属性（使用对象来调用）
        self.name = name



print(Person.name)
per = Person("Tom")
#对象属性的优先级是高于类属性 如果对象属性和类属性同名，优先调用对象属性
print(per.name)
print(Person.name)

#可以动态的给对象添加对象属性 可以在外面添加，也可以在__init__里面添加
per.age = 18
print(per.age)

#删除对象中的name属性，再调用会使用同名的类属性
#注意：对象属性和类属性尽量不要重名，因为对象属性会屏蔽类属性
del per.name
print(per.name)