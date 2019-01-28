#coding=utf-8

from person import Person
from student import Student
from worker import Worker


per = Person("Hanmeimei",20,10)

#创建一个Student对象
stu = Student("Tom",20,100,20181108)
print(stu.name,stu.age,stu.getMoney(),stu.stuID)
stu.run()
stu.eat("apple")
#通过继承过来的公有方法来访问父类的私有属性
stu.setMoney(101)
print(stu.getMoney())


print("***************")
#创建一个Worker对象
wor = Worker("Lilei",20,200)
print(wor.name,wor.age,wor.getMoney())
wor.run()
wor.eat("oringe")
wor.setMoney(201)
print(wor.getMoney())

