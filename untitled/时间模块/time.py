#coding=utf-8
import time

#返回当前时间的时间戳 浮点数形式不需要参数
c = time.time()
print(c)

#将时间戳转为UTC时间元组
t = time.gmtime(c)
print(t)

#将时间戳转为本地时间元组
b = time.localtime(c)
print(b)


#将本地时间元组转换成时间戳
m = time.mktime(b)
print(m)

#将本地时间元组转成时间字符串
s= time.asctime(b)
print(s)

#将时间戳转换成时间字符串
p = time.ctime(c)
print(p)

# 指定格式的时间字符串 --常用
q = time.strftime("%Y-%m-%d %X")
print(q)

#延迟一个时间，整型或者浮点型
#time.sleep(2)
#print("********")

#
#y1 = time.clock()
#print(y1)

#time.sleep(1)
#y2 = time.clock()
#print(y2)

#time.sleep(1)
#y3 = time.clock()
#print(y3)

#示例1--CPU性能测试
print("*********")
time.clock()
sum = 0
for i in range(1000):
    sum += i
print(time.clock())