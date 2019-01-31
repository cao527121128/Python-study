# -*- coding: utf-8 -*-

import tornado.web
import tornado.ioloop
import tornado.httpserver


class IndexHandler(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        self.write("Linuxcao is a good man")


if __name__ == "__main__":

    app = tornado.web.Application([
        (r"/",IndexHandler)
    ])


    #手动实例化一个http服务器
    httpServer = tornado.httpserver.HTTPServer(app)
    #将服务器绑定到指定端口port
    httpServer.bind(8000)
    #默认是开启一个进程，值大于0则创建对应个数的进程，值小于0或者None则开启对应硬件机器的CPU核心个数进程，比如2核心就开启2个进程
    httpServer.start(5)


    tornado.ioloop.IOLoop.current().start()
