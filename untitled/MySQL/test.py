#/usr/bin/python env
#coding=utf-8
'''


'''
from LinuxcaoSql import LinuxcaoSql

s = LinuxcaoSql("localhost","root","qingcloud","Linuxcao")

res = s.get_all("select * from bandcard  where money>400")
for row in res:
    print("%d--%d" %(row[0],row[1]))
