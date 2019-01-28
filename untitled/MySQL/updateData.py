#/usr/bin/python env
#coding=utf-8

import pymysql

#连接数据库
db = pymysql.connect("localhost","root","qingcloud","Linuxcao")

#创建cursor对象
cursor = db.cursor()

#执行sql语句
#修改表bandcard中的数据
sql = "update bandcard set money=1000 where id=1"
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