#coding=utf-8
'''
continue 语句：
功能：跳出当前循环的剩余语句，然后继续下一次循环
注意：跳过距离最近的那一层循环
'''

#
for i in range(10):
    print(i)
    if i == 3:
        continue
    print("*")
    print("&")