#coding=utf-8
#思考：要存储100个人的年龄？
#解决：使用列表
#本质：是一种有序的集合

'''
创建列表
格式：列表名 = [列表选项1，列表选项2，.....列表选项n]
'''
#创建一个空列表
list1 = []
print(list1)

#创建带有元素的列表
list2 = [18, 19, 20, 21, 22]
print(list2)

#注意：列表中的元素数据可以是不同类型的
list3 = [1, 2, "Linuxcao", "good", "man", True]
print(list3)

print("*&*&*&*&*&")
#列表元素的访问  取值和替换
#注意不要越界 （下标超出了可表示的范围）
#取值 格式: 列表名[下标]
list4 = [1, 2, 3, 4, 5]
print(list4[2])

#替换
list4[2] = 300
print(list4)

#计算5个人年龄的平均值
list5 = [18, 19, 20, 21, 22]
index = 0
sum = 0
while index < 5:
    sum += list5[index]
    index += 1
    if index == 5:
        print("平均年龄是%d" % (sum / 5))


#列表的组合
list5 = [1, 2, 3]
list6 = [4, 5, 6]
list7 = list5 + list6
print(list7)

#列表的重复
list8 = [1, 2, 3]
print(list8*3)

#判断元素是否在列表中
list9 = [1,2,3,4]
print(3 in list9)
print(6 in list9)

#列表截取
list10 = [1,2,3,4,5,6,7,8,9,10]
#截取 3 4 5 6
print(list10[2:6])
#截取 3 4 5 6 7 8 9 10
print(list10[2:])
#截取 1 2 3 4
print(list10[:4])

# 二维列表
list11 = [[1,2,3],[4,5,6],[7,8,9]]
# 访问元素5
print(list11[1][1])

#列表方法

# append 在列表末尾添加新的元素
list12 = [1,2,3,4,5]
list12.append(6)
list12.append([7,8,9])
print(list12)

# 在末尾一次性追加另一个列表
list13 = [1,2,3,4,5]
list13.extend([6,7,8])
# list13.extend(6)
print(list13)

#insert
#在下标处添加一个元素，不覆盖原来数据，原数据向后顺延
list14 = [1,2,3,4,5]
list14.insert(2,100)
list14.insert(2,[200,100])
print(list14)

#pop
# 移除列表指定的下标处的元素（默认移除最后一个元素） 并返回删除的数据
list15 = [1,2,3,4,5]
list15.pop(1)
print(list15)
list15.pop()
print(list15)


#remove
#移除列表中某一个元素第一个匹配的结果
list16 = [1,2,3,4,5,6,7,4,5,6,6]
list16.remove(4)
print(list16)


#index
# 从列表中找出某一个值 第一个匹配的索引值
list18 = [1,2,3,4,5,3,4,5,6]
index18 = list18.index(3)
print(index18)
# 固定范围
list19 = [1,2,3,4,5,3,4,5,6]
index19 = list19.index(3,3,8)
print(index19)


#获取列表元素个数
list20 = [1,2,3,4,5]
print(len(list20))

#获取列表元素的最大值
list21 = [1,2,3,4,20]
print(max(list21))

#获取列表元素的最小值
list22 = [1,2,3,4,20]
print(min(list22))


#查看元素在列表中出现的次数
list23 = [1,2,3,4,5,6,5,4,3,2,1]
print(list23.count(3))

#举例
#删除列表中所有元素3
list24 = [1,2,3,4,5,6,5,4,3,2,1]
print(list24.count(3))
num24 = 0
all = list24.count(3)
while num24 < all:
    list24.remove(3)
    num24 += 1
print(list24)


# 倒叙
list25 = [1,2,3,4,5]
list25.reverse()
print(list25)

# 排序
list26 = [1,2,4,3,5]
list26.sort()
print(list26)

# 将元祖转换成列表  (1,2,3,4)  ---> [1,2,3,4]
list31 = list((1,2,3,4))
print(list31)


#实例
#输入10个整数，并且找出第二大数值
listNum = []
num = 0
while num < 10:
    listNum.append(int(input()))
    num += 1
print(listNum)

#首先排序（默认升序）
listNum.sort()
print(listNum)

num1 = 0
all = listNum.count(max(listNum))
listNum_max = max(listNum)
while num1 < all:
    listNum.remove(listNum_max)
    num1 += 1
listNum_second_max = max(listNum)
print(listNum_second_max)



