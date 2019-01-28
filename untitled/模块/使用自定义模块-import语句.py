#coding=utf-8
'''
引入模块
import 语句
格式：
import module1[,module2,module3......modulen]
例如：
import time,random,datetime
 注意：
 1、引入自定义模块 ，不用加.py后缀
 2、同样的模块只会被引入一次不管你执行了多少次import，防止模块被多次引入
import Linuxcao


如何使用模块中的内容？
格式：
模块名.函数名
模块名.变量名


'''
import Linuxcao

#模块名.函数名
Linuxcao.sayGood()
Linuxcao.sayNice()
Linuxcao.sayHandsome()

#模块名.变量名
print(Linuxcao.TT)