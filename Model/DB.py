#coding:utf-8
'''
import the relation moudle1...moduleN
pip_install path:D:\python\Scripts\pip.exe
'''

import MySQLdb
import hashlib
import json
from MySQLdb.cursors import Cursor
from Settings import dbInfo





#(从配置文件中)读取数据库连接的信息 基本的增删改查操作
class dbutils():

        def __init__(self):
            self.name ="db"

        @staticmethod
        def isconnect():
            global conn
            global cursor
            conn = MySQLdb.Connect(dbInfo.DBMS["HOSTNAME"],dbInfo.DBMS["USER"],dbInfo.DBMS["PASSWORD"],dbInfo.DBMS["DB_NAME"],charset='utf8',cursorclass = MySQLdb.cursors.DictCursor)
            print "%s" %conn
            cursor = conn.cursor()
            return conn


        #获取多条数
        @staticmethod
        def query(sql_data,host=3306):
            dbutils.isconnect()
            try:
                query_data = cursor.execute(sql_data)
                data = cursor.fetchall()
                conn.commit()
            except:
                conn.close()
                return data
        #获取一条数据
        @staticmethod
        def get_One(sql_data, host=3306):
            dbutils.isconnect()
            query_data = cursor.execute(sql_data)
            data = cursor.fetchone()
            conn.commit()
            conn.close()
            return data
        #根据指定的个数，批量获取多条数据
        @staticmethod
        def get_Many(sql_data, size,host=3306):
            dbutils.isconnect()
            query_data = cursor.execute(sql_data)
            data = cursor.fetchmany(size)
            conn.commit()
            conn.close()
            return data

        #调用存储过程
        @staticmethod
        def call(callStatement):
            dbutils.isconnect()
            callback =cursor.callproc(callStatement)
            print callback
            return callback


        #对数据库root密码进行md5加密
        def entrypt(self):
            m =hashlib.md5()
            m.update('yiyjaoqaz')
            m.hexdigest()
            return m
