# coding=utf-8
'''
shuzi
数字类型转换
shuzi
'''
#导入库
#库：封装一些功能
#math：数学相关的库
import math
import random

print(int(1.8))
print(float(1))
print(int("123"))
print(float("12.3"))
print(int("+123"))
print(int("-123"))
#print(int("123abc"))

#数学功能
#返回数字的绝对值
a1 = -10
a2 = abs(a1)
print(a2)

# 求x的y次方
print(pow(2,5))

#round
print(round(3.456,2))

#向上取整
print(math.ceil(18.1))
print(math.ceil(18.9))

#向下取整
print(math.floor(18.1))
print(math.floor(18.9))
print(math.floor(18))

#返回整数部分和小数部分
print(math.modf(22.3))

#开方
print(math.sqrt(16))

#随机数
#1 从序列的元素中随机挑选一个元素
print(random.choice([1,3,5,7,9]))
print(random.choice(range(5)))  # range(5) == [0，1,2,3,4]
print(random.choice("linuxcao")) # "linuxcao" == ["l","i","n","u","x","c","a","o"]

#产生一个1~100之间的随机数
r1 = random.choice(range(100)) + 1
print(r1)


#从指定范围内，按指定的基数递增的集合中选取一个随机数
#random.randrange([start,]stop[,step])
#start--指定范围的开始值，包含在范围内，默认是0
#stop -- 指定范围的结束值  不包含在范围内
#step --指定的递增基数，默认是1
r2 = random.randrange(1,100,2)
print(r2)
#从0-99选取一个随机数
r3 = random.randrange(100)
print(r3)


#随机产生[0,1)之间的浮点数
r4 = random.random()
print(r4)

# list
list = [1,3,5,7,9]
#将序列的所有元素随机排序
random.shuffle(list)
print(list)

# 随机生产一个[3,9] 之间的实数
r5 = random.uniform(3,9)
print(r5)




