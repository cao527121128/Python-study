# -*- coding: utf-8 -*-
from __future__ import  absolute_import
import os
import django
from celery import Celery
from django.conf import settings
# os.environ.setdefault(“DJANGO_SETTINGS_MODULE”, “djtest.settings”)
#
# 设置默认的配置文件的环境变量DJANGO_SETTINGS_MODULE，该环境变量的名称，定义在django/conf/_init.py文件里面
#
# ENVIRONMENT_VARIABLE = “DJANGO_SETTINGS_MODULE”
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()
app=Celery('project')
# app.config_from_object()方法从一个配置对象中加载配置
#
# 配置对象可以是一个模块或者任何含有配置属性的对象。
#
# 注意，任何先前设置的配置在调用config_from_object后都会被重新设置。如果你想添加额外的配置，你需要在调用这个方法之后。
app.config_from_object('django.conf.settings')
app.autodiscover_tasks(lambda : settings.INSTALLED_APPS)
#自动发现各个app里面创建的celery任务，可以创建多个任务