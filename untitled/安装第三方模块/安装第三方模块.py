#coding=utf-8


'''
使用pip工具下载安装第三方模块
mac 和 Linux自带pip工具
window：安装python的时候需要勾选pip

要安装第三方模块，就必须要知道第三方模块的名称
'''

# 示例1
#Pillow 非常强大的图像处理的工具库
#pip  install Pillow

#如果出现报错，请先升级pip
#python -m pip install --upgrade pip

# 导入第三方库模块
from PIL import Image

#打开图片
im = Image.open("test.png")

#查看图片信息
print(im.format,im.size,im.mode)
