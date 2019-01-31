#coding:utf-8
from tornado.web import RequestHandler


class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        # self.write("Linuxcao is a handsome man")
        url = self.reverse_url("kaigegood")
        self.write("<a href='%s'>去另一个界面</a>" %(url))

class HomeHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write("This is Home")

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
    # #该方法会在HTTP方法(比如 get post方法)之前调用
    # def initialize(self,word1,word2):
    #     self.word1 = word1
    #     self.word2 = word2

    def get(self, h1,h2,h3,*args, **kwargs):
        # print(self.word1)
        # print(self.word2)
        print(h1+"-"+h2+"-"+h3)
        self.write("Liuyifei is beautiful girl")