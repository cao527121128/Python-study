#coding=utf-8
print("tuple元组")
'''
tuple
本质： 是一种有序的集合
特点：
1、与列表相似
2、一旦初始化就不能修改
3、使用小括号
4、元组相对于列表更加安全  能用元组的尽量用元组不用列表

创建tuple
格式：
元组名 = (元组元素1，元组元素2，......,元组元素n)

'''

#创建空元组
tuple1 = ()
print(tuple1)

#创建带有元素的元组，元组中的元素可以是不同类型的数据
tuple2 = (1,2,3,"good",True)
print(tuple2)

#定义只有一个元素的元组
tuple3 = (1,)
print(tuple3)
print(type(tuple3))


#元组元素的访问
#格式: 元组名[下标]
#下标从0开始
tuple4 = (1,2,3,4,5)
print(tuple4[0])
print(tuple4[1])
print(tuple4[2])
print(tuple4[3])
print(tuple4[4])
#print(tuple4[5])  越界

#获取元组的最后一个元素
print(tuple4[-1])


#修改元组
tuple5 = (1,2,3,4,[5,6,7])
#tuple5[0] = 100         #报错 元组一旦初始化 元组的元素就不可修改
print(tuple5)
#tuple5[-1] = [7,9,10]   #报错 元组一旦初始化 元组的元素就不可修改
print(tuple5)

tuple5[-1][0] = 500      #元组一旦初始化 元组的元素就不可修改，但是如果这个元素是可变的，则可以修改该元素 比如列表
#实际上[5,6,7]在该元组里面存放的是一个内存地址，该内存地址不可变，但是内存地址里面存放的列表元素可以修改
print(tuple5)

#删除元组
tuple6 = (1,2,3)
del tuple6
#print(tuple6)


#元组的操作
#元组相加
t7 = (1,2,3)
t8 = (4,5,6)
t9 = t7 + t8
print(t9)
print(t7,t8)

#元组重复
t10 = (1,2,3)
print(t10 * 3)

#判断元素是否在元组中
t11 = (1,2,3)
print(1 in t11)
print(1 not in t11)
print(4 in t11)
print(4 not in t11)

#元组的截取
#格式：元组名[开始下标：结束下标]
#从开始下标开始截取，截取到结束下标之前
t12 = (1,2,3,4,5,6,7,8,9)
print(t12[3:7])
print(t12[3:])
print(t12[:7])

#二维元组
#元素为一维元组的元组
t13 = ((1,2,3),(4,5,6),(7,8,9))
print(t13[1][1])  #访问5

#元组的方法
#len()
#返回元组中元素的个数
t14 = (1,2,3,4)
print(len(t14))


#max() 返回元组中的最大值
#min() 返回元组中的最小值
print(max((1,2,3,4,5)))
print(min((1,2,3,4,5)))

#将列表转成元组
list = [1,2,3]
t15 = tuple(list)
print(t15)


#元组的遍历
for i in (1,2,3,4,5):
    print(i)