# -*- coding: utf-8 -*-
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#参数
options = {
    "port":9000,
    "list":["good","nice","handsome"]
}

#配置
settings = {
    "debug":True,
    # "autoreload":True,
    # "compiled_templates_cache":False,
    # "static_hash_cache":False,
    # "serve_traceback":True,
    "static":os.path.join(BASE_DIR,"static"),
    "templates":os.path.join(BASE_DIR,"templates"),
}

