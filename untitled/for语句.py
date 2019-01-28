#coding=utf-8
'''
for 语句
格式：
for 变量名 in 集合:
    语句


逻辑：按顺序取“集合”中的每一个元素赋值给"变量"，再去执行语句。如此往复循环，直到取完"集合"中的元素为止
'''
for i in [1,2,3,4,5]:
    print(i)

#range([start,]end[,step])
#功能：生成数列
a = range(10)
print(a)
for x in range(10):
    print(x)

for y in range(2,20,2):
    print(y)

#enumerate 枚举遍历器
#枚举 遍历列表
for index,m in enumerate([1,2,3,4,5]):
    print(index,m)

# 求1+2+..100的和
sum = 0
for n in range(1,101):
    sum += n
print(sum)