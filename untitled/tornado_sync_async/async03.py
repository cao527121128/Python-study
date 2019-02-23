#coding:utf-8
import time
import threading

'''
协程实现异步:使用协程+装饰器实现
'''
global gen

#handler获取数据(数据库、其他服务、循环耗时)
def longIO():
    def run():
        print("开始耗时操作")
        time.sleep(5)
        try:
            global gen
            gen.send("rony is a nice girl")
        except StopIteration as e:
            pass
    threading.Thread(target=run).start()

#reqA()的装饰器
def genCoroutine(func):
    def wrapper(*args,**kwargs):
        # 添加修改的功能
        pass
        global gen
        gen=func(*args,**kwargs)
        next(gen)
    return wrapper

@genCoroutine
def reqA():
    print("开始处理reqA")
    res=yield longIO()
    print("接收到longIO的响应数据:%s" % (res))
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