# coding: utf-8
import tornado.web
import tornado.ioloop
import tornado.httpserver
import config
from application import Application
import  os

if __name__ == "__main__":

    print("port=%d" % (config.options.get("port")))
    print("list=%s" %(config.options.get("list")))

    # BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    # STATIC_DIR = os.path.join(BASE_DIR,"static")
    #
    # print("BASE_DIR==%s" %(BASE_DIR))
    # print("STATIC_DIR==%s" % (STATIC_DIR))
    app = Application()
    httpServer = tornado.httpserver.HTTPServer(app)
    httpServer.bind(config.options.get("port"))
    httpServer.start(1)

    tornado.ioloop.IOLoop.current().start()
