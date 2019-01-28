#coding=utf-8
'''
字典概述：
使用键-值(key-value)存储，具有极快的查找速度

key的特性：
1、字典中的key必须唯一
2、key必须为不可变对象
3、字符串和整数都是不可变对象，可以作为key，一般默认使用字符串作为key
4、list是可变的，不能作为key
5、字典是无序的，没有编号

字典的特点：
1、查找和添加的速度极快，不会随着key-value的增加而变慢
2、需要占用大量的内存，内存浪费多（每存储一个value，必须存储一个key）


list列表的特点：
1、查找和添加的速度会随着key-value的增加而变慢
2、占用空间小，占用的内存小（因为list数据都是紧密排列的，不需要存储无关的数据）



思考：
如何保存多位学生的姓名和成绩？
使用字典
学生姓名为key，学生成绩为值
'''

dict1 = {"tom":60,"lilei":80,"Linuxcao":90}
print("dict1==%s" %(dict1))

#字典元素的访问
#获取：字典名[key]
print(dict1["lilei"])
#print(dict1["Linuxcao"])  #报错 KeyError: 'Linuxcao'
print(dict1.get("Linuxcao"))
ret = dict1.get("Linuxcao")
if ret == None:
    print("没有Linuxcao")
else:
    print("有Linuxcao")
    print("ret==%s" %(ret))


#修改:字典名[key] = value
dict1["lilei"] = 90
print(dict1)

#添加：字典名[新key] = value
dict1["hanmeimei"] = 99
print(dict1)

#删除
#dict1.pop("tom")
#print(dict1)

#遍历
#按key值遍历
for key in dict1:
    print(key,dict1[key])

#按value值遍历
for value in dict1.values():
    print(value)

#按key-value 遍历
for k,v in dict1.items():
    print(k,v)

#枚举编号排序遍历  注意：字典是无序的 在内存中存储是无序的
for i,v2 in enumerate(dict1):
    print(i,v2)

print("*****************")
#字典举例练习
#默认有一组字符串，输入一个单词，返回该单词在这个字符串中出现的次数？
w = "Linuxcao"
#w = input()
d = {}
str = "Linuxcao is a good man! Linuxcao is a nice man! Linuxcao is a handsome man!"
l = str.split()
print(l)
for v in l:
    c = d.get(v)
    if c == None:
        d[v] = 1
    else:
        d[v] += 1
print(d)
print(d[w])