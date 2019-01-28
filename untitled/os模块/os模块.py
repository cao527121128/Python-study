#coding=utf-8
import os
'''
os : 包含了普遍的操作系统的功能

'''

#获取操作系统的类型
#nt --window
#posix--Linux or MacO OS
print(os.name)


#获取操作系统详细的信息  注意只有Linux环境有，window操作系统不支持该方法
#print(os.uname())


#获取操作系统中的所有的环境变量
#print(os.environ)


#获取操作系统中指定的环境变量
print(os.environ.get("TMP"))

#获取当前目录  ./a/
print(os.curdir)

#获取当前工作目录
print(os.getcwd())

#以列表的形式返回指定目录下的所有文件
print(os.listdir(r"E:\study\untitled"))

#创建新目录
#os.mkdir("Linuxcao")  #新目录为相对路径 即为当前目录下创建
#os.mkdir(r"E:\study\untitled\test")  #x新目录为绝对路径

#删除目录
#os.rmdir("Linuxcao")
#os.rmdir(r"E:\study\untitled\test")

#获取文件属性
print(os.stat("Linuxcao"))

#重命名
#os.rename("Rony","Linuxcao")


#删除普通文件
#os.remove(r"E:\study\untitled\file1.txt")

#运行shell命令
#os.system("notepad")  #打开记事本
#os.system("write")    #打开word
#os.system("mspaint")  #打开画板
#os.system("msconfig")  #打开系统配置
#os.system("shutdown -s -t 500") #计划关机注销
#os.system("shutdown -a")  #取消关机注销
#os.system("taskkill /f /im notepad.exe")  #杀掉记事本后台进程


'''
os.path方法
'''
print("*************************")
#示例1--查看当前目录的绝对路径
print(os.path.abspath("."))


#示例2--拼接路径  注意参数2不能以斜杠开头
p1 = r"E:\study\untitled"
p2 = "Linuxcao\Rony"
print(os.path.join(p1,p2))


p3 = "/root/Linuxcao"
p4 = "Rony"
# Linux环境下的结果为：/root/Linuxcao/Rony
print(os.path.join(p3,p4))


#示例3--拆分路径获取文件名
path2 = r"E:\study\untitled\file2.txt"
print(os.path.split(path2))

#示例4--拆分路径获取文件扩展名
print(os.path.splitext(path2))

print("*******************")

#示例5--判断是否是目录
print(os.path.isdir(path2))

#示例6--判断文件是否存在
path3 = r"E:\study\untitled\file4.txt"
print(os.path.isfile(path3))

#示例7--判断目录是否存在
path4 = r"E:\study\untitled"
print(os.path.exists(path4))

#示例8--获取文件大小  返回文件字节大小
print(os.path.getsize(path3))

#示例9--
#获取目录名称
print(os.path.dirname(path3))
#获取文件名称
print(os.path.basename(path3))