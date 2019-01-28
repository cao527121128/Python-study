#coding=utf-8


class Person(object):
    def run(self):
        print("run")
        print(self.__money)
    def eat(self,food):
        print("eat " + food)
    def openDoor(self):
        print("open door")
    def fillEle(self):
        print("fill Ele")
    def closeDoor(self):
        print("close door")
    def __init__(self,name,age,height,weight,money,company,sex):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.__money = money
        self.__company__ = company
        self._sex = sex

        pass
    def __del__(self):
        pass
        #print("这里是析构函数")
    def __str__(self):
        return "%s--%d--%d--%d--%d--%d" %(self.name,self.age,self.height,self.weight,
                                      self.__money,self._sex)

    #通过自定义的方法实现对私有属性的取值和赋值
    #通过内部方法可以修改内部私有属性
    def setMoney(self,money):
        #数据的过滤
        if money < 0:
            money = 0
        self.__money = money

    # 通过内部方法可以访问内部私有属性
    def getMoney(self):
        return self.__money

per = Person("Hanmeimei",20,165,50,10000,"QingCloud",0)

#外部可以直接访问对象内部属性，修改对象内部属性
print(per.age)
per.age = 30
print(per.age)

#如果要让对象内部属性不被外部直接访问和修改，可以在属性前面加两个下划线__
#在python中如果属性前面加两个下划线__，则表明该属性变成私有属性
#print(per.__money)  # 外部直接使用 报错：AttributeError: 'Person' object has no attribute '__money'
#per.run()  #内部可以使用


# 通过自定义的方法实现对私有属性的取值和赋值
print(per)
per.setMoney(1000)
print(per.getMoney())
print(per)

#为何不能直接访问__money ?
#不能直接访问per.__money是因为python解释器把__moeny变成了_Person__money
#我们任然可以使用per._Persion__money访问，但是不建议这么做，因为不同的python解释器
#可能存在解释的变量名不一致的情况
#示例
per._Person__money = 1
print(per.getMoney())


#在python中 __xxxx__属于特殊变量，外部可以直接访问  比如__init__ 但是自己定义的变量一般不这样定义
print(per.__company__)


#在python中 _xxxx属于特殊变量，外部可以直接访问,但是按照约定的规则，当我们看到这样的变量是，
#意思就是“虽然我可以直接外部访问，但是我们一般把它看成私有的，不能在外部直接访问”
print(per._sex)
