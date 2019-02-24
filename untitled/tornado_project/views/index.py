#coding:utf-8
from tornado.web import RequestHandler
from tornado.web import authenticated
import os
import config
import time
from tornado.httpclient import AsyncHTTPClient
from tornado.web import asynchronous
import json
import tornado
from tornado.websocket import WebSocketHandler

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

#数据库操作
class StudentsHandler(RequestHandler):
    def get(self, *args, **kwargs):
        #数据库中插入一条学生信息 sname=linuxcao sage=32  sgrade_id=1
        self.application.db.insert("insert into students (sname,sage,sgrade_id) values ('linuxcao',32,1)")
        self.application.db.insert("insert into students (sname,sage,sgrade_id) values ('linuxcao',33,1)")

        # 数据库中删除一条学生信息 sname=linuxcao sage = 32
        self.application.db.delete("delete from students where sname='linuxcao' and sage=32")

        # 更新数据库  修改姓名为linuxcao的学生的sage=20
        self.application.db.update("update students set sage=20 where sname='linuxcao'")

        #数据库获取students的全部学生信息
        stus = self.application.db.get_all("select * from students")

        # 数据库获取students的第一条学生信息
        # stus = self.application.db.get_one("select * from students")
        print(stus)

        # self.write("ok")
        self.render("students.html",stus = stus)

#普通cookie
class PCookieHandler(RequestHandler):
    def get(self, *args, **kwargs):
        # 设置普通cookie值
        # 函数原型
        # self.set_cookie(name,value,domain=None,expires=None,path="/",expires_days=None,**kwargs)
        self.set_cookie("Linuxcao","good")
        # self.set_header("Set-Cookie","Linuxcao=nice; Path=/")
        self.write("ok")

class GetPCookieHandler(RequestHandler):
    def get(self, *args, **kwargs):
        #获取普通cookie值
        # 函数原型
        # self.get_cookie(name,default=None)
        cookie = self.get_cookie("Linuxcao","未登录")
        print("cookie=%s" %(cookie))
        self.write("ok")

class ClearPCookieHandler(RequestHandler):
    def get(self, *args, **kwargs):
        pass
        #删除名为name的，并且同时匹配path和domain的cookie
        #函数原型
        # self.clear_cookie(name,path="/",domain=None)
        # self.clear_cookie("Linuxcao")

        # 删除同时匹配了path和domain的所有cookie
        # 函数原型
        # self.clear_all_cookies(path="/",domain=None)
        self.clear_all_cookies()
        self.write("ok")

class SCookieHandler(RequestHandler):
    def get(self, *args, **kwargs):
        pass
        # 设置安全cookie
        # 函数原型
        # self.set_secure_cookie(name,value,expires_days=30,version=None,**kwargs)
        self.set_secure_cookie("zhangmanyu","nice")
        self.write("ok")

        # "2|1:0|10:1550046062|10:zhangmanyu|8:bmljZQ==|f041e7e8b983d8eb85e81f2d62ecb40322033fdcee5cdbf38850a69369d09ee7"


class GetSCookieHandler(RequestHandler):
    def get(self, *args, **kwargs):
        pass
        #获取安全cookie
        #函数原型
        # self.get_secure_cookie(name,value=,max_age_days=31,min_version=None)
        scookie = self.get_secure_cookie("zhangmanyu")
        print("scookie=%s" %(scookie))
        self.write("ok")

class CookieNumHandler(RequestHandler):
    def get(self, *args, **kwargs):

        count =self.get_cookie("count",None)
        if not count:
            count = 1
        else:
            count = int(count)
            count += 1
        self.set_cookie("count",str(count))
        self.render("cookienum.html",count=count)


#改进版本
class CookieCountHandler(RequestHandler):
    def get(self, *args, **kwargs):
        pass
        count = self.get_cookie("count","未登录")
        self.render("cookienum.html",count=count)

#将cookie的修改操作放在POST方法里面
class PostHandler(RequestHandler):
    def get(self, *args, **kwargs):
        pass
        self.render("post.html")
    def post(self, *args, **kwargs):
        pass
        count = self.get_cookie("count",None)
        if not count:
            count = 1
        else:
            count = int(count)
            count += 1
        self.set_cookie("count",str(count))
        self.redirect("/cookiecount")


#用户验证
class LoginHandler(RequestHandler):
    def get(self, *args, **kwargs):
        pass
        next = self.get_argument("next","/")
        url = "login?next="+next

        self.render("login.html",url=url)

    def post(self, *args, **kwargs):
        pass
        name = self.get_argument("username")
        pwd = self.get_argument("passwd")
        if name == "admin" and pwd == "qingcloud":
            pass
            next = self.get_argument("next","/")
            self.redirect(next+"?flag=logined")
        else:
            pass
            next = self.get_argument("next","/")
            print(next)
            self.redirect("/login?next="+next)
class HomesHandler(RequestHandler):
    def get_current_user(self):
        flag = self.get_argument("flag",None)
        return flag

    @authenticated
    def get(self, *args, **kwargs):
        pass
        self.render("homes.html")

class CartsHandler(RequestHandler):
    def get_current_user(self):
        flag = self.get_argument("flag",None)
        return flag

    @authenticated
    def get(self, *args, **kwargs):
        pass
        self.render("carts.html")

# 回调函数实现异步web请求
class GetStudents1Handler(RequestHandler):
    def on_response(self,response):
        print("on_response")
        if response.error:
            self.send_error(500)
        else:
            # data = json.loads(response.body)
            data = "rony is a good girl"
            self.write(data)
        #手动关闭通信通道
        self.finish()

    #@tornado.web.asynchronous装饰器作用：不关闭通信通道 get结束之后不自动关闭通信通道,
    # 这样才可以保证回调函数on_response使用self.write(data)返回数据给客户端浏览器
    # 但是需要在on_response中使用finish()手动关闭通信通道
    @tornado.web.asynchronous
    def get(self, *args, **kwargs):
        #获取所有学生的信息
        # time.sleep(30)
        url = "http://rony.qingdesktop.com"
        #创建客户端
        client = AsyncHTTPClient()
        client.fetch(url,self.on_response)
        # self.write("OK")



#协程实现异步web请求
class GetStudents2Handler(RequestHandler):
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        #获取所有学生的信息
        # time.sleep(30)
        url = "http://rony.qingdesktop.com"
        #创建客户端
        client = AsyncHTTPClient()
        res = yield client.fetch(url)
        if res.error:
            self.send_error(500)
        else:
            # data = json.loads(res.body)
            data = "rony is a good girl"
            self.write(data)


#协程实现异步web请求
class GetStudents3Handler(RequestHandler):
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        res = yield self.getData()
        self.write(res)

    #耗时操作写在getData函数里面
    @tornado.gen.coroutine
    def getData(self):
        url = "http://rony.qingdesktop.com"
        # 创建客户端
        client = AsyncHTTPClient()
        res = yield client.fetch(url)
        if res.error:
            ret = {"ret":0}
        else:
            # data = json.loads(res.body)
            data = "rony is a handsome girl"
            ret = data
        raise tornado.gen.Return(ret)  #相当于gen.send()







class GetHomeHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write("Home")

class ChatHomeHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render("chathome.html")

class ChatHandler(WebSocketHandler):
    #所有客户端
    users = []
    def open(self, *args, **kwargs):
        self.users.append(self)
        # print("open")
        # print(self.users)
        for user in self.users:
            #user代表每一个客户端
            #user.write_message() 给每一个客户端发送message数据
            user.write_message("%s 登陆了" %(self.request.remote_ip))

    def on_message(self, message):
        for user in self.users:
            user.write_message(u"%s 说:%s" %(self.request.remote_ip,message))

    def on_close(self):
        self.users.remove(self)
        for user in self.users:
            user.write_message("%s 退出了" %(self.request.remote_ip))

    def close(self, code=None, reason=None):
        pass

    def check_origin(self, origin):
        return True
