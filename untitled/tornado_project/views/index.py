#coding:utf-8
from tornado.web import RequestHandler
import os
import config

class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        # self.write("Linuxcao is a handsome man")
        url = self.reverse_url("kaigegood")
        self.write("<a href='%s'>去另一个界面</a>" %(url))

# class HomeHandler(RequestHandler):
#     def get(self, *args, **kwargs):
#         self.write("This is Home")

class LinuxcaoHandler(RequestHandler):
    #该方法会在HTTP方法(比如 get post方法)之前调用
    def initialize(self,word1,word2):
        self.word1 = word1
        self.word2 = word2

    def get(self, *args, **kwargs):
        print(self.word1)
        print(self.word2)
        self.write("This is Linuxcao")

class KaigeHandler(RequestHandler):
    #该方法会在HTTP方法(比如 get post方法)之前调用
    def initialize(self,word3,word4):
        self.word3 = word3
        self.word4 = word4

    def get(self, *args, **kwargs):
        print(self.word3)
        print(self.word4)
        self.write("This is Kaige")

class LiuyifeiHandler(RequestHandler):
    def get(self, h1,h2,h3,*args, **kwargs):
        print(h1+"-"+h2+"-"+h3)
        self.write("Liuyifei is beautiful girl")


class ZhangmanyuHandler(RequestHandler):
    def get(self,*args, **kwargs):
        # self.get_query_argument(name,default=ARG_DEFAULT,strip=True)
        # self.get_query_argument('a',default=ARG_DEFAULT,strip=True)
        # 127.0.0.1:8000/zhangmanyu?a=1&b=2&c=3
        # a = self.get_query_argument('a')
        # b = self.get_query_argument('b')
        # c = self.get_query_argument('c')
        # print(a+"-"+b+"-"+c)

        #127.0.0.1:8000/zhangmanyu?a=1&a=2
        # self.get_query_arguments(name,strip=True)
        alist = self.get_query_arguments("a")
        print(alist[0]+"-"+alist[1])

        self.write("Zhangmanyu is good woman")

class PostFileHandler(RequestHandler):
    #展示get页面
    def get(self,*args, **kwargs):
        self.render('postfile.html')

    #接收post数据
    def post(self,*args, **kwargs):
        username = self.get_body_argument("username")
        passwd = self.get_body_argument("passwd")
        hobbyList = self.get_body_arguments("hobby")
        print(username + "-" + passwd)
        print(hobbyList)
        self.write("Linuxcao is a good man")


class ZhuyinHandler(RequestHandler):

    def get(self,*args, **kwargs):
        print(self.request.method)
        print(self.request.host)
        print(self.request.uri)
        print(self.request.path)
        print(self.request.query)
        print(self.request.version)
        print(self.request.headers)
        print(self.request.body)
        print(self.request.remote_ip)
        print(self.request.files)


        self.write("Zhuyin is beautiful girl")

class UpFileHandler(RequestHandler):

    def get(self,*args, **kwargs):
        self.render("upfile.html")

    def post(self, *args, **kwargs):
        # files = self.request.files
        # print(files)
        filesDict = self.request.files
        for inputname in filesDict:
            fileArr= filesDict[inputname]
            for fileObj in fileArr:
                #存储路径
                filePath = os.path.join(config.BASE_DIR,'upfile/'+ fileObj.filename)
                with open(filePath,"wb") as f:
                    f.write(fileObj.body)
            self.write("ok")

class WriteHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write("Linuxcao is a good man")
        self.write("Linuxcao is a nice man")
        self.write("Linuxcao is a handsome man")
        #刷新缓存区 关闭当次请求通道
        #默认在finish后面就不要写write 即使写了write也不会输出响应
        self.finish()
        self.write("Linuxcao is a cool man")

#json
import json
class JsonHandler(RequestHandler):
    def get(self, *args, **kwargs):
        per = {
            "name":"Linuxcao",
            "age":32,
            "height":170,
            "weight":65
        }
        #将字典转换成json字符串
        jsonStr = json.dumps(per)
        self.set_header("Content-Type","application/json; charset=UTF-8")
        self.set_header("Linuxcao","good")
        self.write(jsonStr)

class Json2Handler(RequestHandler):
    def get(self, *args, **kwargs):
        per = {
            "name":"rony",
            "age":31,
            "height":168,
            "weight":55
        }
        self.write(per)


#header
class HeaderHandler(RequestHandler):
    def set_default_headers(self):
        self.set_header("Content-Type","application/json; charset=UTF-8")
        self.set_header("Linuxcao","good")
    def get(self, *args, **kwargs):
        # self.set_header("Linuxcao","nice")
        self.write("Linuxcao is a good man")
    def post(self, *args, **kwargs):
        pass


#status
class StatusCodeHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.set_status(404)
        # self.set_status(999,"who? where? what?")
        # self.set_status(999)
        self.write("**********")
    def post(self, *args, **kwargs):
        pass



#redirect
class RedirectHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.redirect("/")


#错误处理
#send_error and  write_error
class ErrorHandler(RequestHandler):
    def write_error(self, status_code, **kwargs):
        if status_code == 500:
            code = 500
            #返回500错误界面
            self.write("服务器内部错误")
        elif status_code == 404:
            code = 404
            #返回404错误界面
            self.write("资源不存在")
        self.set_status(code)
    def get(self, *args, **kwargs):
        flag = self.get_query_argument("flag")
        print(type(flag))
        if flag == "0":
            # self.send_error(500)
            self.send_error(404)
        self.write("you are right")

#接口调用顺序
class Index1Handler(RequestHandler):
    def initialize(self):
        print("initialize")

    def prepare(self):
        print("prepare")

    def get(self, *args, **kwargs):
        print("HTTP method=GET")
        self.send_error(500)
        self.write("Linuxcao is a good man")

    def set_default_headers(self):
        print("set_default_headers")

    def write_error(self, status_code, **kwargs):
        print("write_error")
        self.write("服务器内部错误")

    def on_finish(self):
        print("on_finish")


#模板
class HomeHandler(RequestHandler):
    def get(self, *args, **kwargs):
        temp = 100
        per = {
            "name": "rony",
            "age": 31,
            "height": 168,
            "weight": 55
        }
        flag = 0
        stus = [
            {
                "name":"lilei",
                "age":18
            },
            {
                "name":"hanmeimei",
                "age":19
            }
        ]
        self.render("home.html",num=temp,per=per,flag=flag,stus=stus)


#自定义函数
class FuncHandler(RequestHandler):
    def get(self, *args, **kwargs):
        pass
        def mySum(n1,n2):
            return n1+n2
        self.render("market.html",ms=mySum)


#转义
class TransHandler(RequestHandler):
    def get(self, *args, **kwargs):
        str = "<h1>Linuxcao is a good man</h1>"
        self.render("trans.html",str=str)


#继承
class CartHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render("cart.html",title="cart")