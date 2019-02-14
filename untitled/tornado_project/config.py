# -*- coding: utf-8 -*-
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#参数
options = {
    "port":9000,
    "list":["good","nice","handsome"]
}


#数据库配置
mysql = {
    "host":"127.0.0.1",
    "user":"root",
    "passwd":"qingcloud",
    "dbName":"Linuxcao",
    "port":3306

}
#配置
settings = {
    "debug":True,
    # "autoreload":True,
    #"compiled_templates_cache":False,
    # "static_hash_cache":False,
    # "serve_traceback":True,
    "static_path":os.path.join(BASE_DIR,"static"),
    "template_path":os.path.join(BASE_DIR,"templates"),
    # "autoescape":None,
    "cookie_secret":"XX7KhLy0Sleq8PRIRKXv2KMIn4p80EuJk48jcz15LMU",
    "xsrf_cookies":True,
    "login_url":"/login"
}

