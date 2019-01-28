#coding=utf-8
'''
什么是字符串？
字符串是以单引号或者双引号括起来的任意文本
'abc'
"def"
记住：字符串是不可变的！
'''

#创建字符串
str1 = "Linuxcao is a good man!"
str3 = "Linuxcao is a nice man!"
str5 = "Linuxcao is a handsome man!"
print(str1)
print(str3)
print(str5)

'''
字符串运算
'''
#字符串连接
str6 = "Linuxcao is"
str7 = "a good man!"
str8 = str6 + str7
print("str6=",str6)
print("str7=",str7)
print("str8=",str8)
print "str8=",str8

#输出重复字符串
str9 = "good"
str10 = str9 * 3
print("str10=",str10)

#访问字符串中的某一个字符
#通过索引下标查找字符，索引从0开始
#字符串名[下标]
#比如查找第二个字符 i
str11 = "Linuxcao is a good man!"
print(str11[1])
#str11[1] = "a"  #字符串是不可变的
print("str11=",str11)


#截取字符串中的一部分
str13 = "Linuxcao is a good man!"
#从给定下标处开始截取到给定下标之前
str15 = str13[12:22]
print("str15=",str15)

#从头截取到给定下标之前
str16 = str13[:12]
print("str16=",str16)

#从给定下标处开始截取到结尾处
str17 = str13[14:]
print("str17=",str17)

#结合成员运算符
str18 = "Linuxcao is a good man!"
print("Linuxcao" in str18)
print("Linuxcao1" not in str18)


#格式化输出
# %d %s %f  占位符  占一个位置的意思
print("Linuxcao is a good man!")
num = 10
str19 = "Linuxcao is a nice man!"
f =  10.123456789
#print("num =",num,"str19=",str19)
print("num = %d,str19 = %s,f = %.3f" %(num,str19,f))

#转义字符 \
'''
转义字符：将一些字符转换成有特殊含义的字符

'''
# \n 换行
print("num = %d\nstr19 = %s\nf = %.3f" % (num,str19,f))
print("Linuxcao is a  \\n  good man!")

# Linuxcao is a 'good' man
print("Linuxcao is a \'good\' man!")
print('Linuxcao is a \"good\" man!')

# 如果字符串里面有多个\n 则可以直接使用'''代替打印
print("good\nnice\nhandsome\n")
print('''
good
nice
handsome
''')

#\t 制表符
print("Linuxcao \tis a good man")

#如果字符串中有好多字符需要转义，就需要加入很多/
#python允许使用r 表示内部的字符串默认不转义
#\\\t\t\t
print(r"\\t\t\t")
# E:\study\untitled
print(r"E:\study\tuntitled")
print("E:\study\\tuntitled")


#eval
#功能：将字符串str当成有效的表达式来求值，并返回表达式的计算结果
num1 = eval("123")
print("num1 = %d" % num1)
print(type(num1))

#num1 = int("123")
#print("num1 = %d" % num1)
#print(type(num1))

print(eval("+123"))
print(eval("-123"))
print(eval("12+3"))
print(eval("12-3"))
#print(eval("12a3"))


# len(str)
# 返回字符串的长度（字符个数）
print(len("Linuxcao is a good man!"))


#lower()
# 转换字符串中的大写字母为小写字母
str20 = "Linuxcao is a GOOD man"
print(str20.lower())
print(str20)

str21 = str20.lower()
print(str20)
print(str21)

#upper
# 转换字符串中的小写字母为大写字母
str22 = "Linuxcao is a GOOD man"
str23 = str22.upper()
print("str22 = %s,str23 = %s" %(str22,str23))

#swapcase
#转换字符串中的小写字母为大写字母，大写字母转小写字母
str23 = "Linuxcao is a GOOD man"
print(str23.swapcase())

#capitalize()
#首字母大写，其他小写
str23 = "LINUXCAO is a GOOD man"
print(str23.capitalize())

#title()
#每个单词的首字母为大写，其他小写
str24 = "LinuXCAO iS a gOOd mAn"
print(str24.title())

#center(width[,fillchar])  character
#返回一个指定宽度的居中字符串，fillchar为填充的字符串，默认空格填充
str25 = "Linuxcao is a nice man"
print(str25.center(40,"*"))

#ljust(width[,fillchar])  character
#返回一个指定宽度的左对齐字符串，fillchar为填充的字符串，默认空格填充
str26 = "Linuxcao is a nice man"
print(str26.ljust(40,"*"))

#rjust(width[,fillchar])  character
#返回一个指定宽度的右对齐字符串，fillchar为填充的字符串，默认空格填充
str27 = "Linuxcao is a nice man"
print(str27.rjust(40,"*"))


#zfill(width)
#返回一个长度为width的字符串，原字符串右对齐，前面补0
str28 = "Linuxcao is a nice man"
print(str28.zfill(40))

# count(str[,start][,end])
str29 = "Linuxcao is very very nice man!"
print(str29.count("very",15,len(str29)))


#find(str[,start][,end])
#从左到右检测str是否包含在字符串中，可以指定查找范围（start，end）
#默认从头到尾，得到第一次出现的开始下标，没有则返回-1
str30 = "Linuxcao is very very nice man!"
print(str30.find("very",0,len(str30)))
print(str30.find("verdy",0,len(str30)))


#rfind(str[,start][,end])
#从右到左检测str是否包含在字符串中，可以指定查找范围（start，end）
#默认从头到尾，得到第一次出现的开始下标，没有则返回-1
str30 = "Linuxcao is very very nice man!"
print(str30.rfind("very",0,len(str30)))
print(str30.rfind("verdy",0,len(str30)))

#index(str[,start][,end])
#从左到右检测str是否包含在字符串中，可以指定查找范围（start，end）
#默认从头到尾，得到第一次出现的开始下标，没有则返回一个报错 ValueError: substring not found
str31 = "Linuxcao is very very nice man!"
print(str31.index("very",0,len(str30)))
#print(str31.index("verdy",0,len(str30)))

#rindex(str[,start][,end])
#从右到左检测str是否包含在字符串中，可以指定查找范围（start，end）
#默认从头到尾，得到第一次出现的开始下标，没有则返回一个报错 ValueError: substring not found
str32 = "Linuxcao is very very nice man!"
print(str32.rindex("very",0,len(str30)))
#print(str32.rindex("verdy",0,len(str30)))


#lstrip()
#截取字符串左侧指定的字符，默认为空格
str33 = "        Linuxcao is very very nice man!"
print(str33.lstrip())
str33 = "********Linuxcao is very very nice man!"
print(str33.lstrip("*"))


#rstrip()
#截取字符串右侧指定的字符，默认为空格
str34 = "Linuxcao is very very nice man!        "
print(str34.rstrip())
str34 = "Linuxcao is very very nice man!*********"
print(str34.rstrip("*"))

# strip()
#截取字符串左右两侧指定的字符，默认为空格
str35 = "          Linuxcao is very very nice man!      "
print(str35.strip())
str35 = "**********Linuxcao is very very nice man!******"
print(str35.strip("*"))

str36 = 'a'
print(ord(str36))
str37 = chr(65)
print(str37)


#split(str)
#以str为分隔符截取字符串
#例如求一组字符串中单词个数？
str38 = "Linuxcao****is****a***good**man"
list39 = str38.split("*")
print(list39)
c = 0
for s in list39:
    if len(s) > 0:
        c += 1
print(c)

#splitlines(keepends) 按照（'\n' '\r'  '\r\n'）分割字符串  分割成list
#keepends == True则会保留换行符  默认为flash不保留换行符
str40 = '''Linuxcao is a good man!
Linuxcao is a nice man!
Linuxcao is a handsome man!
'''
print(str40.splitlines())

#join(seq) 以指定的字符串分隔符，将seq中的所有元素组合成一个字符串
list41 = ["Linuxcao","is","a","good","man"]
str41 = "*&*".join(list41)
print(str41)

#max() min()
str43 = "Linuxcao is a good man!"
print(max(str43))
print("*" + min(str43) + "*")


#replace(oldstr,newstr[,count])
#用newstr替换oldstr，默认是全部替换，如果指定了count个数，则只替换前面count个
str44 = "Linuxcao is a good good good man!"
str45 = str44.replace("good","nice")
print(str44)
print(str45)

#startswith(str)
#判断该字符串是否以str开头
str49 = "Linuxcao is a good man!"
print(str49.startswith("Linuxcao"))

#endswith(str)
#判断该字符串是否以str结尾
str50 = "Linuxcao is a good man!"
print(str50.endswith("man!"))

#编码
#encode(encoding="utf-8",error="strict")
str51 = "Linuxcao is a good man!"
data52 = str51.encode("utf-8")
print(data52)

#解码
#注意：要与编码时使用的编码格式保持一致
str53 = data52.decode("utf-8")
print(str53)


#isalpha()
#如果字符串中至少有一个字符，且所有的字符都是字母则返回True，否则返回False
str54 = "Linuxcao is a good man!"
print(str54.isalpha())
str54 = "Linuxcaoisagoodman"
print(str54.isalpha())

#isalnum()
#如果字符串中至少有一个字符，且所有的字符都是字母或者数字则返回True，否则返回False
str55 = "12&Linuxcao"
print(str55.isalnum())
str55 = "12Linuxcao"
print(str55.isalnum())

print("*************")
#isupper()
#如果字符串中至少有一个英文字符，且所有英文字符都是大写英文字符则返回True，否则返回False
print("ABC".isupper())
print("ABC1".isupper())
print("ABC&^&^".isupper())
print("ABC&^&^a".isupper())


print("*************")
#islower()
#如果字符串中至少有一个英文字符，且所有英文字符都是小写英文字符则返回True，否则返回False
print("abc".islower())
print("abcD".islower())
print("abc13&*&*".islower())
print("12".islower())


print("*************")
#istitle()
#如果字符串是标题化（单词首字母是大写的）的则返回True，否则返回False
print("Linuxcao Is".istitle())
print("Linuxcao is".istitle())
print("linuxcao is".istitle())

print("*************")
#isdigit()
#如果字符串只包含数字的则返回True,否则返回False
print("123".isdigit())
print("A123".isdigit())

print("*************")
#isspace()
#如果字符串中只包含空格，则返回True,否则返回False
print("123".isspace())
print("   ".isspace())
print("\n".isspace())
print("\t".isspace())