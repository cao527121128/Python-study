#coding=utf-8
import os

def getAllDirDEP(path):
    mystack = []
    mystack.append(path)
    print(mystack)
    #处理栈，当栈为空的时候结束循环
    while len(mystack) != 0:
        path = mystack.pop()  # 取出路径
        #print(path)
        filelist = os.listdir(path)  # 遍历路径
        #print(filelist)

        for filename in filelist:
            filepath = os.path.join(path, filename)  # 连接，取得绝对路径

            if os.path.isdir(filepath):
                print("Dir", filename)
                #print(filepath)
                mystack.append(filepath)
            else:
                print("File", filename)


path = r"E:\study\untitled\Scripts\test"
print("遍历的顶层目录 == %s" % (path))
getAllDirDEP(path)