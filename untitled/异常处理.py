#coding=utf-8
'''
try.....except.....else

格式：
try:
    语句t
except 错误码 as e:
    语句1
except 错误码 as e：
    语句2
.......
except  错误码 as e:
    语句n
else:
    语句e



注意： else语句可有可无
作用：用来检测try语句块中的错误，从而让except语句捕获错误信息并处理异常
需求：当程序遇到问题时不想让程序结束，而是越过错误继续向下执行

逻辑：当程序执行到try-execept-else语句时
1、如果try语句t执行出现错误，会匹配第一个错误码，如果匹配上就执行对应语句
2、如果try语句t执行出现错误，没有匹配到错误码，错误会被提交到上一层的try语句，或者程序的最上层
3、如果try语句t执行没有出现错误，执行else下的语句e （前提是末尾有else语句e）

.........



'''

#示例1--最完整示例
try:
    #print(3 / 0)
    print(3 / 1)
    #print(num)
except ZeroDivisionError as e:
    print("除数为0")
except NameError as e:
    print("没有该变量")
else:
    print("代码没有问题")
print("****************")


#示例2--使用except但是不带错误码
try:
    print(4 / 0)
except:
    print("程序出现了异常")

print("*****************")


#示例3--使用except带有多个异常错误码
try:
    print(4 / 0)
    pass
except (ZeroDivisionError,NameError):
    print("出现了异常ZeroDivisionError,NameError")


print("***********************")


#示例4--使用错误异常基类BaseExcept可以捕获所有异常情况
#错误其实是class类，所有的错误都继承自BaseException 所以在捕获的时候，他捕获了该类型的错误，还把子类的错误异常也一网打尽
try:
    print(4 / 0)
    pass
except BaseException as e:
    print("BaseException 异常")
except ZeroDivisionError as e:
    print("出现了异常ZeroDivisionError异常")

print("***********")
#示例5--跨越多层调用
#main调用了func2  func2调用了func1 ，而func1出现了错误，这时只要main捕获到了异常信息就可以处理异常
def func1(num):
    print(1 / num)

def func2(num):
    func1(num)

def main():
    func2(0)

try:
    main()
except ZeroDivisionError as e:
    print("出现了异常ZeroDivisionError")



'''
try.....except.....finally

格式：
try:
    语句t
except 错误码 as e:
    语句1
except 错误码 as e：
    语句2
.......
except  错误码 as e:
    语句n
finally:
    语句f



逻辑：与上面try.....except....else逻辑类似
唯一区别：语句t无论是否有错误，都将执行最后的语句f

应用场景：文件打开，Linux默认只能打开1024个文件描述符，如果超过1024就无法继续打开，所有每次打开文件之后，
无论是否成功打开文件，都必须执行关闭文件描述符的操作（此时就需要finally语句）

'''
print("&&&&&&&&&&")
#示例1--
try:
    print(1 / 0)
except ZeroDivisionError as e:
    print("ZeroDivisionError异常")
finally:
    print("必须执行我")