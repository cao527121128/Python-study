#coding=utf-8

#值传递：传递的参数是不可变类型
#比如字符串、元组、set、number等
def func1(num):
    num = 10
temp =20
func1(temp)
print(temp)

#引用传递：传递的参数是可变类型
#比如list、dict、set是可变的

def func2(lis):
    lis[0] = 200
li = [1,2,3,4]
func2(li)
print(li)