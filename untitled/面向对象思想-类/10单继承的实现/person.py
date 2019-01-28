# coding=utf-8

class Person(object):
    def __init__(self, name,age,money):
        self.name = name
        self.age = age
        self.__money = money

    def run(self):
        print("run")

    def eat(self,food):
        print("eat " + food)

    def getMoney(self):
        return self.__money

    def setMoney(self,money):
        self.__money = money


