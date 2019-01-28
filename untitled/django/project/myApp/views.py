# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect

# Create your views here.

from django.http import HttpResponse,HttpResponseRedirect

#重定向 到主页
def index_html(request):
    return HttpResponseRedirect('/sunck')

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
    studentsList = Students.stuObj2.all()
    #将数据传递给模板，模板再渲染页面，并将渲染好的页面返回给浏览器
    return render(request,'myApp/students.html',{"students":studentsList})

def students2(request):
    #去模型中取数据
    #如果没有找到符合条件的对象，则返回"模型类.DoesNotExist"异常
    studentsList = Students.stuObj2.get(sname = 'Linuxcao')

    #如果找到多条符合条件的对象，则返回"模型类.MutilpleObjectsReturned"异常
    #studentsList = Students.stuObj2.get(sgender= True)
    #将数据传递给模板，模板再渲染页面，并将渲染好的页面返回给浏览器
    return HttpResponse("XXXXXXXXXXXXXXXX")

# 显示前5条数据
def students3(request):
    #去模型中取数据
    studentsList = Students.stuObj2.all()[0:5]
    #将数据传递给模板，模板再渲染页面，并将渲染好的页面返回给浏览器
    return render(request,'myApp/students.html',{"students":studentsList})


# 分页显示 每一页显示5条数据

def stupage(request,page):
    # 0-5  5-10  10-15
    # page=1 显示 0-5
    # page=2 显示 5-10
    # page=3 显示 10-15
    page = int(page)
    #去模型中取数据
    studentsList = Students.stuObj2.all()[(page-1)*5:page*5]
    #将数据传递给模板，模板再渲染页面，并将渲染好的页面返回给浏览器
    return render(request,'myApp/students.html',{"students":studentsList})


from django.db.models import Max
def studentsearch(request):

    #查询所有名字包含"zhang'的学生信息
    #studentsList = Students.stuObj2.filter(sname__contains='zhang')
    #studentsList = Students.stuObj2.filter(sname__startswith='zhang')
    #查询pk值在[2,4,6,8]范围的学生信息
    #studentsList = Students.stuObj2.filter(pk__in=[2,4,6,8])
    #查询年龄大于30的学生信息
    #studentsList = Students.stuObj2.filter(sage__gt=30)
    # 查询最后修改时间日期是2017年的学生信息
    studentsList = Students.stuObj2.filter(lastTime__year=2017)

    maxAge = Students.stuObj2.aggregate(Max('sage'))
    print(maxAge)
    # 将数据传递给模板，模板再渲染页面，并将渲染好的页面返回给浏览器
    return render(request,'myApp/students.html',{"students":studentsList})



def gradesStudents(request,num):
    #获取指定的班级
    grade = Grades.objects.get(pk=num)
    #获取指定班级的所有学生信息
    studentsList = grade.students_set.all()
    # 将数据传递给模板，模板再渲染页面，并将渲染好的页面返回给浏览器
    return render(request,'myApp/students.html',{"students":studentsList})


def addstudent(request):
    #获取指定的班级
    grade = Grades.objects.get(pk=1)
    #创建学生对象
    stu = Students.createStudent('liudehua',True,58,'i am liudehua',grade,'2019-01-25','2019-01-25')
    stu.save()

    # 去模型中取数据 应该包含新添加的'liudehua'
    studentsList = Students.stuObj2.all()
    # 将数据传递给模板，模板再渲染页面，并将渲染好的页面返回给浏览器
    return render(request,'myApp/students.html',{"students":studentsList})

def addstudent2(request):
    #获取指定的班级
    grade = Grades.objects.get(pk=1)
    #创建学生对象
    stu = Students.stuObj2.createStudent('zhangxueyou',True,53,'i am zhangxueyou',grade,'2019-01-25','2019-01-25')
    stu.save()

    # 去模型中取数据 应该包含新添加的'liudehua'
    studentsList = Students.stuObj2.all()
    # 将数据传递给模板，模板再渲染页面，并将渲染好的页面返回给浏览器
    return render(request,'myApp/students.html',{"students":studentsList})

from django.db.models import F,Q
def fgrades(request):
    #F对象：模型的A属性和B属性进行比较
    #返回女生个数大于男生个数的班级
    #g = Grades.objects.filter(ggirlnum__gt=F('gboynum'))
    #返回女生个数大于男生个数+10的班级
    g = Grades.objects.filter(ggirlnum__gt=F('gboynum')+10)
    print(g)
    return HttpResponse("000000000000")

def qstudents(request):

    # 返回 pk <=3 或者 年龄大于50的学生
    #studentsList = Students.stuObj2.filter(Q(pk__lte=3) | Q(sage__gt=50))
    #返回Pk<=3的学生
    #studentsList = Students.stuObj2.filter(Q(pk__lte=3))
    #返回pk >3的学生
    studentsList = Students.stuObj2.filter(~Q(pk__lte=3))
    # 将数据传递给模板，模板再渲染页面，并将渲染好的页面返回给浏览器
    return render(request, 'myApp/students.html', {"students": studentsList})

def attribles(request):
    print(request.path)
    print(request.method)
    print(request.encoding)
    print(request.GET)
    print(request.POST)
    print(request.FILES)
    print(request.COOKIES)
    print(request.session)
    return HttpResponse("attribles")

#GET 属性
def get1(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    c = request.GET.get('c')
    return HttpResponse(a + "   " + b + "   " + c)

def get2(request):
    a = request.GET.getlist('a')
    a1 = a[0]
    a2 = a[1]
    c = request.GET.get('c')
    return HttpResponse(a1 + "   " + a2 + "   " + c)

#POST属性
def showregist(request):
    return render(request,'myApp/regist.html')

def regist(request):
    name = request.POST.get('name')
    gender = request.POST.get('gender')
    age = request.POST.get('age')
    hobby = request.POST.getlist('hobby')
    print(name)
    print(gender)
    print(age)
    print(hobby)

    return HttpResponse("regist")

#response
def showresponse(request):
    res = HttpResponse()
    res.content = b'linuxcao is a good man'
    print(res.content)
    print(res.charset)
    print(res.status_code)
    #print(res.content-type)
    return res

# cookie
def cookietest(request):
    res = HttpResponse()
    res.set_cookie('sunck','he is a good man')
    return res

def showcookie(request):
    res = HttpResponse()
    cookie = request.COOKIES
    res.write("<h1>"+cookie['sunck']+"</h1>")
    return res

# 重定向
from django.http import HttpResponseRedirect
from django.shortcuts import  redirect

def redirect1(request):
    #标准方式：使用HttpResponseRedirect
    #return HttpResponseRedirect('/sunck/redirect2')

    #简写方式：使用redirect
    return redirect('/sunck/redirect2')

def redirect2(request):
    return HttpResponse('我是重定向之后的视图')

# session
def main(request):
    #根据session-key 获取 session-value session键值
    username = request.session.get('name',"游客")
    return render(request,'myApp/main.html',{'username':username})

def login(request):

    return render(request,'myApp/login.html')

def  showmain(request):

    username = request.POST.get('username')

    #在服务端 django创建的HttpRequest对象request中存储session值
    request.session['name'] = username
    #request.session.set_expiry(10)
    return HttpResponseRedirect('/sunck/main/')

from django.contrib.auth import logout
def quit(request):
    #清除session
    logout(request)
    #request.session.clear()
    #request.session.flush()
    return HttpResponseRedirect('/sunck/main/')


def index1(request):
    student = Students.objects.get(pk=1)
    students_list = Students.objects.all()
    num1 = 10
    num2 = 10
    str = "Linuxcao is a nice man"
    return render(request,'myApp/index1.html',{"num":10,"stu":student,"students":students_list,"num1":num1,"num2":num2,
                                               "str":str})


