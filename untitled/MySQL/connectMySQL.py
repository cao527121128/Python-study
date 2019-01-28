#/usr/bin/env python
#coding=utf-8
import pymysql
#参数1: mysql服务所在主机的IP
#参数2：用户名
#参数3：密码
#参数4：要连接的数据库名
#连接数据库
db = pymysql.connect("localhost","root","qingcloud","Linuxcao")

#创建一个cursor对象
cursor = db.cursor()


#执行sql语句
#sql = "select version();"    代码中可以不用加分号末尾
sql = "select version()"
cursor.execute(sql)

#获取返回信息
data = cursor.fetchone()
print(data)

#断开数据库连接
cursor.close()
db.close()