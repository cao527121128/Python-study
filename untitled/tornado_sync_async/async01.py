#coding:utf-8
import time
import threading


'''
回调函数实现异步
'''
#handler获取数据(数据库、其他服务、循环耗时)
def longIO(callback):
    def run(cb):
        print("开始耗时操作")
        time.sleep(5)
        print("结束耗时操作")
        cb("rony is a nice girl")
    threading.Thread(target=run,args=(callback,)).start()


#回调函数实现异步
def finish(data):
    print("开始处理回调函数")
    print("接收到longIO的响应数据:%s" %(data))
    print("结束处理回调函数")

#一个客户端的请求
def reqA():
    print("开始处理reqA")
    #longIO成功结束了之后，才会回调执行finish函数
    longIO(finish)
    print("结束处理reqA")

#另一个客户端的请求
def reqB():
    print("开始处理reqB")
    time.sleep(2)
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