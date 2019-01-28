#coding=utf-8

from cat import Cat
from mouse import Mouse
from animal import Animal

class Person(object):

    def feedCat(self,cat):
        print("给你食物")
        cat.eat()

    def feedMouse(self,mouse):
        print("给你食物")
        mouse.eat()

    def feedAnimal(self,ani):
        print("给你食物")
        ani.eat()
