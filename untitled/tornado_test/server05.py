# -*- coding: utf-8 -*-

import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options

# tornado.options.define("port",default=9000,type=int,help=None,metavar=None,multiple=None,group=None,callback=None)
#定义两个参数
tornado.options.define("port",8000,int)
tornado.options.define("list",[],str,multiple=True)

class IndexHandler(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        self.write("Linuxcao is a good man")


if __name__ == "__main__":
    #转换配置文件的参数 并保存到tornado.options.options
    tornado.options.parse_config_file("config")
    print("port=%s" % (tornado.options.options.port))
    print("list=%s" %(tornado.options.options.list))
    # tornado.options.options.logging = None
    app = tornado.web.Application([
        (r"/",IndexHandler)
    ])



    httpServer = tornado.httpserver.HTTPServer(app)
    httpServer.bind(tornado.options.options.port)
    httpServer.start(1)


    tornado.ioloop.IOLoop.current().start()
