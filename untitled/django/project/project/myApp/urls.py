#coding=utf-8
from django.conf.urls import url,include

from . import views

# r 不使用任何转义字符
# ^$  以空字符开头，以空字符结尾  也即是什么都不输入

urlpatterns = [
    url(r'^$', views.index),
    url(r'^(\d+)/(\d+)/$', views.detail),
    url(r'^grades/$', views.grades),
    url(r'^students/$', views.students),
    url(r'^grades/(\d+)$',views.gradesStudents),
]
