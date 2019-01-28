#coding=utf-8
"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin



#r 不使用任何转义
# ^admin 表示以admin字符开头
# ^ 表示以空字符开头
# 127.0.0.1:8000/admin 匹配  r'^admin/'  页面转到 admin管理界面
# 127.0.0.1:8000/ 匹配  r'^'  页面转到 myApp.urls      而myApp.urls中 url(r'^$', views.index),  继续匹配到views.index 页面


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^sunck/', include('myApp.urls',namespace="app")),
]

