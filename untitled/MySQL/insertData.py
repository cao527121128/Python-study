#/usr/bin/python env
#coding=utf-8

import pymysql

#连接数据库
db = pymysql.connect("localhost","root","qingcloud","Linuxcao")

#创建cursor对象
cursor = db.cursor()

#执行sql语句
#在表bandcard里面插入数据
sql = "insert into bandcard VALUES(0,100),(0,200),(0,300),(0,400),(0,500),(0,600)"
try:
    cursor.execute(sql)
    db.commit()
except:
    #如果提交失败，回滚到上一次数据
    db.rollback()

#获取返回信息
data = cursor.fetchone()
print(data)

#断开数据库连接
cursor.close()
db.close()