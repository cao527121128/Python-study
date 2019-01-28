#coding=utf-8
import win32con

import win32gui

import random

import time

#示例2--控制窗体的位置和大小
#QQwin = win32gui.FindWindow("TXGuiFoundation","QQ")
#win32gui.SetWindowPos(QQwin,win32con.HWND_TOP,100,100,300,300,win32con.SWP_SHOWWINDOW)

#小括号中的参数（控制的窗体，大致方位（HWND_TOP上方），位置X，位置Y，长度，宽度，（显示））


#示例3--QQ满屏随机动

while True:
    x = random.randrange(1800)

    y = random.randrange(100)

    QQwin = win32gui.FindWindow("TXGuiFoundation","QQ")

    win32gui.SetWindowPos(QQwin,win32con.HWND_TOP,x,y,300,300,win32con.SWP_SHOWWINDOW)
