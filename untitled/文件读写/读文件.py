#coding=utf-8
'''
过程：
1、打开文件
2、读取文件内容
3、关闭文件

'''

'''
1、打开文件
open(path,flag[,encoding,errors])
path:要打开文件的路径
flag:打开方式
r   以只读的方式打开文件，文件的描述符放在文件的开头
rb  以二进制的格式打开一个文件用于只读，文件的描述符放在文件的开头
r+  以读写的方式打开文件，文件的描述符放在文件的开头

w   打开一个文件只用于写入，如果该文件已经存在则覆盖，如果不存在则创建新文件
wb  打开一个文件只用于写入二进制，如果该文件已经存在则覆盖，如果不存在则创建新文件
w+  打开一个文件只用于读写，如果该文件已经存在则覆盖，如果不存在则创建新文件
a   打开一个文件用于追加，如果该文件存在，文件描述符将会放在文件末尾，如果不存在则创建新文件
a+  打开一个文件用于读写，如果该文件存在，文件描述符将会放在文件末尾（此时只能写入，读取是没有任何数据的），
如果不存在则创建新文件 
 
encoding: 编码方式  utf-8
errors: 错误处理  ignore

'''

#示例1 --打开文件
path = r"E:\study\untitled\file1.txt"
f = open(path,"r")
print("*****")


'''
2、读文件内容
'''
#1、读取文件全部内容（适用于文件内容比较少的）   --常用
#str1 = f.read()
#print(str1)

#2 读取指定字符数
#str2 = f.read(10)
#print("*" + str2 + "*")

#str3 = f.read(10)
#print("*" + str3 + "*")

#3 读取整行，包括“\n" 字符            --常用
#str4 = f.readline()
#print(str4)

#str5 = f.readline()
#print(str5)

#4 读取指定字符数  -与2类似
#str6 = f.readline(10)
#print(str6)

#5 读取所有行并返回列表        --常用
#list7 = f.readlines()
#print(list7)

#6 修改文件描述符--从指定位置开始读取文件内容
str8 = f.read()
print(str8)
print("&&&&&&&")
f.seek(10)
str9 = f.read()
print(str9)

'''
3、关闭文件
'''
f.close()

print("**************")
#示例1--一个完整的标准过程
try:
    f1 = open(path,"r")
    str10 = f1.read()
    print(str10)
finally:
    if f1:
        f1.close()

print("$$$$$$$$$$$$$")
#示例2--示例1的缩减版本
#读完文件之后，无论成功或者失败，with都会自动关闭文件
with open(path,"r") as f2:
    print(f2.read())