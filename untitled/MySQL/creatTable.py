#/usr/bin/python env
#coding=utf-8

import pymysql

#连接数据库
db = pymysql.connect("localhost","root","qingcloud","Linuxcao")

#创建cursor对象
cursor = db.cursor()

#执行sql语句
#检测表是否已经存在，如果存在则删除
cursor.execute("drop table if exists bandcard")
#创建表bandcard
sql = "create table bandcard(id int auto_increment primary key,money int not null)"
cursor.execute(sql)


#获取返回信息
data = cursor.fetchone()
print(data)

#断开数据库连接
cursor.close()
db.close()