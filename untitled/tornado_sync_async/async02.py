#coding:utf-8
import time
import threading

'''
协程实现异步：使用协程实现
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



#一个客户端的请求
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
    global gen
    gen=reqA() #生成一个生成器
    # 执行reqA ,但是只执行到res=yield longIO() reqA被挂起，创建线程处理耗时操作，同时主程序继续向下执行reqB
    # 当longIO执行完毕之后，会再次唤醒reqA 继续执行res=yield longIO() ，res接收gen.send()返回的数据
    next(gen)
    reqB()
    while 1:
        time.sleep(0.1)
        pass

if __name__ == '__main__':
    main()