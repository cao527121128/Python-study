#coding=utf-8
from django.conf.urls import url,include

from . import views

# r 不使用任何转义字符
# ^$  以空字符开头，以空字符结尾  也即是什么都不输入

urlpatterns = [
    url(r'^$', views.index),
    url(r'^index.html/$', views.index_html),
    url(r'^(\d+)/(\d+)/$', views.detail),
    url(r'^grades/$', views.grades),
    url(r'^students/$', views.students),
    url(r'^grades/(\d+)$',views.gradesStudents),
    url(r'^addstudent/$',views.addstudent),
    url(r'^addstudent2/$', views.addstudent2),
    url(r'^students2/$', views.students2),
    url(r'^students3/$', views.students3),
    url(r'^stupage/(\d+)/$', views.stupage),
    url(r'^studentsearch/$', views.studentsearch),
    url(r'^fgrades/$', views.fgrades),
    url(r'^qstudents/$', views.qstudents),
    url(r'^grades/$', views.grades,name="grades"),
    url(r'^attribles/$', views.attribles),
    url(r'^get1/$', views.get1),
    url(r'^get2/$', views.get2),
    url(r'^showregist/$',views.showregist),
    url(r'^showregist/regist/$',views.regist),
    url(r'^showresponse/$',views.showresponse),
    url(r'^cookietest/$',views.cookietest),
    url(r'^showcookie/$',views.showcookie),
    url(r'^redirect1/$',views.redirect1),
    url(r'^redirect2/$',views.redirect2),
    url(r'^main/$',views.main),
    url(r'^login/$', views.login),
    url(r'^showmain/$',views.showmain),
    url(r'^quit/$',views.quit),
    url(r'^index1/$',views.index1),
]
