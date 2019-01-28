#coding=utf-8
'''
人
类名：Person
属性：gun
行为：fire

枪
类名：Gun
属性：bulletBox
行为: shoot

弹夹
类名: BulletBox
属性：bulletCount

'''
from person import Person
from gun import Gun
from bulletbox import BulletBox

#创建一个弹夹对象
bul = BulletBox(5)


#创建一个枪对象
gun = Gun(bul)

#创建一个人对象
per = Person(gun)

#人开枪射击子弹
per.fire()
per.fire()
per.fire()
per.fire()
per.fire()
per.fire()


#人弹夹填充子弹
per.fillBullet(2)
per.fire()
per.fire()
per.fire()