#coding=utf-8
import win32con

import win32gui

import random

import time

# 示例1--使qq不停的显示隐藏（不停的闪烁效果）
while True:

    #获取QQ窗体的编号
    QQwin = win32gui.FindWindow("TXGuiFoundation","QQ")
    #QQwin = win32gui.FindWindow("Chrome_WidgetWin_1", "新标签页-Google Chrome")

    #隐藏QQ窗体
    win32gui.ShowWindow(QQwin,win32con.SW_HIDE)

    time.sleep(1)

    #显示QQ窗体
    win32gui.ShowWindow(QQwin,win32con.SW_SHOW)

    time.sleep(1)


