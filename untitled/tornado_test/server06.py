# -*- coding: utf-8 -*-

import tornado.web
import tornado.ioloop
import tornado.httpserver
import config


class IndexHandler(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        self.write("Linuxcao is a good man")


if __name__ == "__main__":

    print("port=%d" % (config.options.get("port")))
    print("list=%s" %(config.options.get("list")))
    app = tornado.web.Application([
        (r"/",IndexHandler)
    ])



    httpServer = tornado.httpserver.HTTPServer(app)
    httpServer.bind(config.options.get("port"))
    httpServer.start(1)


    tornado.ioloop.IOLoop.current().start()
