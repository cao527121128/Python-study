#/usr/bin/python env
#coding=utf-8

'''

fetchone()
功能：获取下一个查询结果集，结果集是一个对象

fetchall()
功能：接收全部的返回行
'''
import pymysql

#连接数据库
db = pymysql.connect("localhost","root","qingcloud","Linuxcao")

#创建cursor对象
cursor = db.cursor()

#执行sql语句
#查找bandcard表中money大于400的数据
sql = "select * from bandcard where money>400"
try:
    cursor.execute(sql)
    reslist = cursor.fetchall()
    for row in reslist:
        print("%d--%d" %(row[0],row[1]))
except:
    print("find error!")
    #如果提交失败，回滚到上一次数据
    db.rollback()

#获取返回信息
data = cursor.fetchone()
print(data)

#断开数据库连接
cursor.close()
db.close()