#coding=utf-8

import os

def getAllDirDRE(path,sp):
    #得到当前目录下的所有文件
    filesList = os.listdir(path)
    #处理每一个文件
    sp = sp + " "
    for fileName in filesList:
        #print(fileName)
        #拼接成绝对路径
        fileAbsPath = os.path.join(path,fileName)
        if os.path.isdir(fileAbsPath):
            print(sp + "dir:%s" %(fileName))
            getAllDirDRE(fileAbsPath,sp)
        else:
            print(sp + "files:%s" %(fileName))

path = r"E:\study\untitled\Scripts\test"
print("遍历的顶层目录 == %s" % (path))
getAllDirDRE(path,sp=" ")

