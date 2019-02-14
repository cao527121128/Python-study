# coding=utf-8
import tornado.web
from views import index
import config
import os
from sunckMysql import SunckMySQL

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

            #数据库
            (r'/students',index.StudentsHandler),

            # 设置普通cookie
            (r'/pcookie', index.PCookieHandler),

            # 获取普通cookie
            (r'/getpcookie', index.GetPCookieHandler),

            # 清除普通cookie
            (r'/clearpcookie',index.ClearPCookieHandler),

            # 设置安全cookie
            (r'/scookie', index.SCookieHandler),

            # 获取安全cookie
            (r'/getscookie', index.GetSCookieHandler),

            #cookie计数 记录浏览器访问次数
            (r'/cookienum',index.CookieNumHandler),

            # cookie计数 记录浏览器访问次数 改进版本
            (r'/cookiecount', index.CookieCountHandler),
            (r'/post',index.PostHandler),

            #用户验证
            (r'/login',index.LoginHandler),
            (r'/homes',index.HomesHandler),
            (r'/carts', index.CartsHandler),

            #StaticFileHandler 要放在所有匹配路由的最下面
            # r'/(.*)$'  表示匹配任何路由
            # 告诉StaticFileHandler其中path目录中寻找静态文件
            (r'/(.*)$',tornado.web.StaticFileHandler,
             {
                "path":os.path.join(config.BASE_DIR,"static/html"),
                "default_filename":"index.html"
             }),
        ]
        super(Application,self).__init__(handlers,**config.settings)

        self.db = SunckMySQL(config.mysql["host"],config.mysql["user"],config.mysql["passwd"],config.mysql["dbName"],config.mysql["port"])









