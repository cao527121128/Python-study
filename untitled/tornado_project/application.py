# coding=utf-8
import tornado.web
from views import index
import config

class Application(tornado.web.Application):
    def  __init__(self):
        handlers = [
            (r'/',index.IndexHandler),
            (r'/home',index.HomeHandler),
            (r'/linuxcao',index.LinuxcaoHandler,{"word1":"good","word2":"nice"}),
            tornado.web.url(r'/kaige', index.KaigeHandler, {"word3": "handsome", "word4": "cool"},name="kaigegood"),
            (r'/liuyifei/(\w+)/(\w+)/(\w+)', index.LiuyifeiHandler),
        ]
        super(Application,self).__init__(handlers,**config.settings)