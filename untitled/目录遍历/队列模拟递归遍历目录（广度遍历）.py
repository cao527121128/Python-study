#coding=utf-8
import os
import collections


def getAllDirQU(path):
    queue = collections.deque()  # 创建一个队列
    print(queue)
    # 进队
    queue.append(path)
    print(queue)

    while len(queue) != 0:
        # 出队数据
        dirPath = queue.popleft()
        print(dirPath)
        # 找出所有的文件
        filesList = os.listdir(dirPath)

        for fileName in filesList:
            # 绝对路径
            fileAbsPath = os.path.join(dirPath, fileName)
            # 判断是否是目录，是目录就进队，不是就打印
            if os.path.isdir(fileAbsPath):
                print("Dir:", fileName)
                queue.append(fileAbsPath)
            else:
                print("File:", fileName)

path = r"E:\study\untitled\Scripts\test"
print("遍历的顶层目录 == %s" % (path))
getAllDirQU(path)


