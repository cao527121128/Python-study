#coding=utf-8

#引入模块
import sys  #适用于黑屏终端中使用

# sys.argv 获取命令行参数
for i in sys.argv:
    print(i)

name = sys.argv[1]
age = sys.argv[2]
sex = sys.argv[3]


# 自动查找所需模块的路径的列表
print(sys.path)