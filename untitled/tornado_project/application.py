# coding=utf-8
import tornado.web
from views import index
import config
import os

class Application(tornado.web.Application):
    def  __init__(self):
        handlers = [
            # (r'/',index.IndexHandler),
            (r'/linuxcao',index.LinuxcaoHandler,{"word1":"good","word2":"nice"}),
            tornado.web.url(r'/kaige', index.KaigeHandler, {"word3": "handsome", "word4": "cool"},name="kaigegood"),
            #提取uri特定部分
            (r'/liuyifei/(\w+)/(\w+)/(\w+)', index.LiuyifeiHandler),

            # get方式传递参数(比如查询字符串)
            (r'/zhangmanyu', index.ZhangmanyuHandler),

            # post方式传递参数(请求体携带数据)
            (r'/postfile', index.PostFileHandler),

            #request对象
            #http://127.0.0.1:9000/zhuyin?a=1
            (r'/zhuyin',index.ZhuyinHandler),

            #上传文件
            (r'/upfile', index.UpFileHandler),

            # write
            (r'/write', index.WriteHandler),

            #json
            (r'/json',index.JsonHandler),

            #json2
            (r'/json2',index.Json2Handler),

            #headers
            (r'/header',index.HeaderHandler),

            #status
            (r'/status',index.StatusCodeHandler),

            #redirect
            (r'/index',index.RedirectHandler),

            #send_error & write_error
            #iserror?flag=0
            (r'/iserror',index.ErrorHandler),

            #
            (r'/index1',index.Index1Handler),

            #模板
            (r'/home',index.HomeHandler),

            #自定义函数
            (r'/function',index.FuncHandler),

            #转义
            (r'/trans',index.TransHandler),

            #继承
            (r'/cart',index.CartHandler),

            #StaticFileHandler 要放在所有匹配路由的最下面
            (r'/(.*)$',tornado.web.StaticFileHandler,
             {
                "path":os.path.join(config.BASE_DIR,"static/html"),
                "default_filename":"index.html"
             }),
        ]
        super(Application,self).__init__(handlers,**config.settings)