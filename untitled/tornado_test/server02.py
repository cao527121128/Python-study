# -*- coding: utf-8 -*-
#tornado 的基础web框架模块
import tornado.web

#tornado的核心IO循环模块 封装了Linux的epoll和BSD的kqueue 队列，是tornado高效的基础
import tornado.ioloop

import tornado.httpserver

#类比django中的views视图函数
class IndexHandler(tornado.web.RequestHandler):
    #处理get请求 不能处理post请求
    def get(self, *args, **kwargs):
        #对应http的请求方法 给浏览器响应数据
        self.write("Linuxcao is a good man")


if __name__ == "__main__":
    #类比django中的urls.py分配器路由
    #实例化一个app对象
    #Application是tornado web框架的一个核心应用类，是与服务器对应的接口
    #里面保存路由映射表，其中有一个listen方法用来创建一个http服务器的实例
    #并绑定了端口-默认8000
    app = tornado.web.Application([
        (r"/",IndexHandler)
    ])
    # app.listen(8000) 创建服务器并绑定监听端口
    #注意：此时服务器并没有开启监听
    #app.listen(8000)

    #也可以手动创建服务器
    #手动实例化一个http服务器
    httpServer = tornado.httpserver.HTTPServer(app)
    #绑定端口
    httpServer.listen(8000)


    #IOLoop.current():返回当前线程的IOLoop实例
    #IOLoop.start() : 启动IOLoop实例的I/0循环 同时开启了监听
    tornado.ioloop.IOLoop.current().start()
