# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from models import Grades,Students



class StudentsInfo(admin.TabularInline):
    model = Students
    extra = 2

#注册方式1：使用装饰器注册  推荐使用装饰器方法注册
@admin.register(Grades)
class GradesAdmin(admin.ModelAdmin):
    #增加学生信息 关联对象
    inlines = [StudentsInfo]

    #列表页属性
    list_display = ['pk','gname','gdate','ggirlnum','gboynum','isDelete']
    list_filter = ['gname']
    search_fields = ['gname']
    list_per_page = 5

    #添加、修改页属性
    #fields = ['ggirlnum','gboynum','gname','gdate','isDelete']
    fieldsets = [
    ("num",{"fields":['ggirlnum','gboynum']}),
    ("base",{"fields":['gname','gdate','isDelete']})
    ]
#注册方式2：使用admin.site.register方法注册
#admin.site.register(Grades,GradesAdmin)




#注册方式1：使用装饰器注册
@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    def gender(self):
        if self.sgender:
            return "男"
        else:
            return "女"
    gender.short_description = "性别"


    #执行动作的位置
    actions_on_bottom = True
    actions_on_top = False
    #列表页属性
    list_display = ['pk','sname',gender,'sage','scontend','isDelete']
    list_filter = ['sname']
    search_fields = ['sname']
    list_per_page = 5

    #添加、修改页属性
    #fields = ['sname','sage','scontend','sgender','sgrade','isDelete']
    fieldsets = [
    ("base",{"fields":['sname','sage','sgender','sgrade']}),
    ("contend",{"fields":['scontend','isDelete']})
    ]
#注册方式2：使用admin.site.register方法注册
#admin.site.register(Students,StudentsAdmin)
