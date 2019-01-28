#coding=utf-8
'''
while 语句
格式：
while 表达式:
    语句


'''
#打印1--5的值
num = 1
while num <= 5:
    print(num)
    num += 1

#计算1+2+3.....100的值
num1 = 1
sum = 0
while num1 <= 100:
    sum += num1
    num1 += 1
print("sum = %d" % (sum))

# str = "Linuxcao is a handsome man" 将字符串的每一个字符都打印出来
str = "Linuxcao is a handsome man"
index = 0
while index < len(str):
    print("str[%d] = %s" % (index,str[index]))
    index += 1


#午间练习
#打印出三位数中所有的水仙花数
num1 = 100
while num1 <= 999:
    a = num1 % 10
    b = num1 // 10 % 10
    c = num1 // 100
    if num1 == a**3 + b**3 + c**3:
        print("num1 =%d" % (num1))
    num1 += 1
'''
#判断输入的整数是否为质数？
num2 = int(input("请输入一个整数："))
if num2 == 2:
    print("是质数")
index = 2
while index < num2:
    if num2 % index == 0:
        print("不是质数")
    index += 1
'''
# 计算输入的字符串中所有数字的和
str = "Linuxca123dafd"
index = 0
sum = 0
while index < len(str):
    if str[index] >= "0" and str[index] <= "9":
        sum += int(str[index])
    index += 1
print("sum = %d" % (sum))


#举例：
# 计算出一组字符串中有多少个单词 （以空格为区分）
str = "   linuxcao is a good man     "
print("str = %s" % (str))
str1 = str.strip()
print("str1 = %s" % (str1))
index = 0
count = 0
while index < len(str1):
    while str1[index] != " ":
        index += 1
        if index == len(str1):
            break

    count  += 1
    print("count = %d" % (count))

    if index == len(str1):
        break
    while str1[index] == " ":
        index += 1

print("count = %d" % (count))



'''
格式：
while 表达式：
    语句1
else:
    语句2


逻辑：在条件语句（表达式）为False时执行else后面的语句

'''

a = 1
while a <= 3:
    print("Linuxcao is a good man!")
    a += 1
else:
    print("very very good!")


#死循环：表达式永远为真的循环
#while 1:
#    print("Linuxcao is a good man!")