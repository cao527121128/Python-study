# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("caolinfeng is a good man")


def detail(request,num,num2):
    return HttpResponse("detail-%s-%s" %(num,num2))

from models import Grades
def grades(request):
    #去模型中取数据
    gradesList = Grades.objects.all()
    #将数据传递给模板，模板再渲染页面，并将渲染好的页面返回给浏览器
    return render(request,'myApp/grades.html',{"grades":gradesList})

from models import Students
def students(request):
    #去模型中取数据
    studentsList = Students.objects.all()
    #将数据传递给模板，模板再渲染页面，并将渲染好的页面返回给浏览器
    return render(request,'myApp/students.html',{"students":studentsList})



def gradesStudents(request,num):
    #获取指定的班级
    grade = Grades.objects.get(pk=num)
    #获取指定班级的所有学生信息
    studentsList = grade.students_set.all()
    # 将数据传递给模板，模板再渲染页面，并将渲染好的页面返回给浏览器
    return render(request,'myApp/students.html',{"students":studentsList})