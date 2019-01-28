#coding=utf-8

#从控制台输入一个整数，判断是否为偶数
num = input()
if num % 2 == 0:
    print("是偶数")
else:
    print("是奇数")

# 判断是否为水仙花数
#153
num1 = input("请输入一个三位数")
a = num1 % 10  #个位数
b = num1 // 10 % 10 #十位数
c = num1 // 100  #百位数
if num1 == a**3 + b**3 + c**3:
    print("yes")
else:
    print("no")

num2 = int(input())
num3 = int(input())
num4 = int(input())
max = num2
if num3 > max:
    max = num3
if num4 > max:
    max = num4

print("max =",max)





