#coding=utf-8
'''

'''
import pickle  #数据持久性模块  意思就是数据直接写入磁盘中

# 示例
# 写入 列表list
myList = [1,2,3,4,5,"Linuxcao is a good man"]
path = r"E:\study\untitled\file6.txt"
f = open(path,"wb")
pickle.dump(myList,f)
f.close()

# 读取 列表list
f1 = open(path,"rb")
tempList = pickle.load(f1)
print(tempList)
f1.close()