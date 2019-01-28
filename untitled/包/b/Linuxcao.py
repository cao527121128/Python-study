#coding=utf-8
#一个.py文件就是一个模块
'''
每一个模块都有一个__name__属性，当其值等于“__main__”时候，表明该模块自身在执行
当前py文件如果是程序入口文件，则__name__的属性就是__main__
当前py文件如果是被其他模块引入调用，则__name__的属性就是它的模块名 比如Linuxcao
'''

if __name__ == "__main__":
    print(__name__)
    print("这是Linuxcao")

else:
    print(__name__)
    def sayGood():
        print("Linuxcao is a good man!")


    def sayNice():
        print("Linuxcao is a nice man!")


    def sayHandsome():
        print("Linuxcao is a handsome man!")

