#coding=utf-8

#示例1
def func(num,div):
    assert(div != 0),"div不能为0"
    return num / div

print(func(10,0))