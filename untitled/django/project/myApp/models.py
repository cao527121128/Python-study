# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Grades(models.Model):
    gname = models.CharField(max_length=20)
    gdate = models.DateTimeField()
    ggirlnum = models.IntegerField()
    gboynum = models.IntegerField()
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return self.gname
    class Meta:
        db_table = "grades"
        ordering = ['-id']


class StudentsManager(models.Manager):
    def get_queryset(self):
        #将isDelete=False的过滤，返回没有删除的数据
        # super(StudentsManager, self).get_queryset()  查询集
        # filter(isDelete=False) 过滤器
        return super(StudentsManager, self).get_queryset().filter(isDelete=False)
    #在自定义管理器中添加方法来创建对象
    def createStudent(self,name,gender,age,contend,grade,lastT,createT,isD=False):
        stu = self.model()
        print(type(stu))
        stu.sname = name
        stu.sgender = gender
        stu.sage = age
        stu.scontend = contend
        stu.sgrade = grade
        stu.lastTime = lastT
        stu.createTime = createT
        return stu

class Students(models.Model):
    #定义一个类方法创建对象
    @classmethod
    def createStudent(cls,name,gender,age,contend,grade,lastT,createT,isD=False):
        stu = cls(sname = name, sgender = gender, sage = age, scontend = contend,
                  sgrade = grade, lastTime = lastT, createTime = createT,isDelete = isD)
        return stu



    #自定义模型管理器
    #当自定义了模型管理器，则默认的objects就不存在了
    #stuObj = models.Manager()
    #stuObj2 = StudentsManager()

    sname = models.CharField(max_length=20)
    sgender = models.BooleanField(default=True)
    sage =models.IntegerField()
    scontend = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)
    #关联外键
    sgrade = models.ForeignKey("Grades")
    lastTime = models.DateTimeField(auto_now=True)
    createTime = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.sname

    class Meta:
        db_table = "students"
        ordering = ['id']

    def  getName(self):
        return self.sname