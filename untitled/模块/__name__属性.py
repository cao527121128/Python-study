#coding=utf-8
'''
__name__属性：
模块就是一个py文件，一个模块被另一个程序引入，但是我不想让模块中的某些代码被执行，可以使用__name__属性
来使程序仅调用模块中的一部分代码
每一个模块都有一个__name__属性，当其值等于“__main__”时候，表明该模块自身在执行
当前py文件如果是程序入口文件，则__name__的属性就是__main__
当前py文件如果是被其他模块引入调用，则__name__的属性就是它的模块名 比如Linuxcao

'''

import Linuxcao

def main():
    print("*********")
    pass




if __name__ == "__main__":
    main()
