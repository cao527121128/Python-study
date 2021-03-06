#/usr/bin/python env
#coding=utf-8

import pymysql
class LinuxcaoSql():
    def __init__(self,host,user,password,dbName):
        self.host = host
        self.user = user
        self.password =password
        self.dbName = dbName
    def connect(self):
        self.db  = pymysql.connect(self.host,self.user,self.password,self.dbName)
        self.cursor = self.db.cursor()
    def close(self):
        self.cursor.close()
        self.db.close()

    #查询一条数据
    def get_one(self,sql):
        res = None
        try:
            self.connect()
            self.cursor.execute(sql)
            res = self.cursor.fetchone()
            self.close()
        except:
            print("查询失败")
        return res

    # 查询多条数据
    def get_all(self, sql):
        res = ()
        try:
            self.connect()
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            self.close()
        except:
            print("查询失败")
        return res

    #插入数据
    def insert(self,sql):
        return self.__edit(sql)

    #修改数据
    def update(self,sql):
        return self.__edit(sql)

    #删除数据
    def delete(self,sql):
        return self.__edit(sql)

    def __edit(self,sql):
        count = 0
        try:
            self.connect()
            count = self.cursor.execute(sql)
            self.db.commit()
            self.close()
        except:
            print("事务提交失败")
            self.db.rollback()
        return count


