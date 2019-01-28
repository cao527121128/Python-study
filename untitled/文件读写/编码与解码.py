# coding=utf-8
'''

'''

# 示例1
# 编码
path = r"E:\study\untitled\file4.txt"
# 以二进制的格式写入utf-8 编码数据
with open(path,"wb") as f1:
    str = "Linuxcao is a good man!"
    f1.write(str.encode("utf-8"))

#解码
with open(path,"rb") as f2:
    data = f2.read()
    print(data)
    print(type(data))

    newData = data.decode("utf-8")
    print(newData)
    print(type(newData))

