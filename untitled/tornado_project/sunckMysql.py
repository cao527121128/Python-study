# -*- coding:utf-8 -*-
import pymysql

class SunckMySQL():
    def __init__(self,host,user,password,database,port):
        self.host=host
        self.user=user
        self.passwd=password
        self.dbName=database
        self.port=port

    def connect(self):
        self.db = pymysql.connect(self.host,self.user,self.passwd,self.dbName,self.port)
        self.cursor=self.db.cursor()

    def close(self):
        self.cursor.close()
        self.db.close()

    def get_one(self,sql):
        res=None
        try:
            self.connect()
            self.cursor.execute(sql)
            res=self.cursor.fetchone()
        except Exception as e:
            print(e)
            print("查询失败")
        finally:
            self.close()
        return res

    def get_all(self,sql):
        res=()
        try:
            self.connect()
            self.cursor.execute(sql)
            res=self.cursor.fetchall()
        except Exception as e:
            print(e)
            print("查询失败")
        finally:
            self.close()
        return res

    def insert(self,sql):
        count=0
        try:
            self.connect()
            count=self.cursor.execute(sql)
            print("插入数据成功")
            self.db.commit()
        except Exception as e:
            print(e)
            print("插入数据失败")
            self.db.rollback()
        finally:
            self.close()
        return count

    def update(self,sql):
        count = 0
        try:
            self.connect()
            count = self.cursor.execute(sql)
            print("数据更新成功")
            self.db.commit()
        except Exception as e:
            print(e)
            print("数据更新失败")
            self.db.rollback()
        finally:
            self.close()
        return count

    def delete(self,sql):
        count = 0
        try:
            self.connect()
            count = self.cursor.execute(sql)
            print("删除数据成功")
            self.db.commit()
        except Exception as e:
            print(e)
            print("数据删除失败")
            self.db.rollback()
        finally:
            self.close()
        return count
