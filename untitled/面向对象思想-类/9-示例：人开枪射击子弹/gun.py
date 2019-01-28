# coding=utf-8

class Gun(object):
    def __init__(self, bulletBox):
        self.bulletBox = bulletBox

    def shoot(self):
        if self.bulletBox.bulletCount == 0:
            print("bullet none")
        else:
            self.bulletBox.bulletCount -= 1
            print("剩余 bullet %d 发" %(self.bulletBox.bulletCount))

