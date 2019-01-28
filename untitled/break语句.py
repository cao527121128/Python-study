#coding=utf-8
'''
break 语句：
功能：跳出for和while循环
注意：只能跳出距离它最近的那一层循环


'''

#循环打印1-10 遇到5自动结束循环
for i in range(10):
    print(i)
    if i == 5:
        break

#while -else
#while循环语句可以有else语句，但是如果是break导致的while循环截止，则不会执行else下面的语句
num = 1
while num <= 10:
    print(num)
    if num == 3:
        break
    num += 1
else:
    print("Linuxcao is a good man!")

