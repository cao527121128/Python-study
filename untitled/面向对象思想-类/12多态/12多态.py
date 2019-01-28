#coding=utf-8
'''
多态：一种事物的多种形态  继承是多态的前提

'''

from cat import Cat
from mouse import  Mouse
from person import Person

#思考如何添加100中动物，每一种动物都有name属性和eat方法
#可以自定义一个有name属性和eat方法的Animal父类，让所有动物都继承自Animal父类即可
tom = Cat("tom")
jerry = Mouse("jerry")

tom.eat()
jerry.eat()

#思考人要喂cat 和 mouse吃食物
per = Person()
per.feedCat(tom)
per.feedMouse(jerry)


print("**********")
#思考人要喂100种动物，难道要写100个feed方法？
per = Person()
per.feedAnimal(tom)
per.feedAnimal(jerry)

