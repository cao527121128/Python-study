#coding:utf-8
import time

#耗时操作 比如handler从数据库中获取数据的操作
def longIO():
    print("开始耗时操作")
    time.sleep(5)
    print("结束耗时操作")
    return "Linuxcao is a good man"



#一个客户端的请求
def reqA():
    print("开始处理reqA")
    res=longIO()
    print("接收到longIO的响应数据:%s" %(res))
    print("结束处理reqA")

#另一个客户端的请求
def reqB():
    print("开始处理reqB")
    print("结束处理reqB")

#tornado服务
def main():
    reqA()
    reqB()
    while 1:
        time.sleep(0.1)
        pass

if __name__ == '__main__':
    main()