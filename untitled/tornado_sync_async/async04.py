#coding:utf-8
import time
import threading

'''
协程实现异步:使用协程+装饰器实现
这个例子是tornado可以实现异步高效处理的原理
'''


#handler获取数据(数据库、其他服务、循环耗时)
def longIO():
    print("开始耗时操作")
    time.sleep(5)
    print("结束耗时操作")
    #返回数据
    yield "rony is a nice girl"


#reqA()的装饰器
def genCoroutine(func):
    def wrapper(*args,**kwargs):
        gen1 = func()  #reqA的生成器
        gen2 = next(gen1) #longIO的生成器
        def run(g):
            res = next(g)  #这里实际上就是执行longIO 并且挂起
            try:
                gen1.send(res) #longIo执行完毕之后，唤醒reqA 将数据返回给reqA
            except StopIteration as e:
                pass
        threading.Thread(target=run,args=(gen2,)).start()
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