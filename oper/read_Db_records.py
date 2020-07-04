#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pymysql
import records
import threading
import time
from oper import read_Config
config = read_Config.ReadConfig()
# 打开数据库连接（ip/端口/数据库用户名/登录密码/数据库名/编码）
# db = pymysql.connect(host="localhost", port=3306, user="root", password="123", db="test", charset='utf8')
# # 使用 cursor() 方法创建一个游标对象 cursor
# cursor = db.cursor()
# # 使用 execute()  方法执行 SQL 查询（查询mysql的版本）
# cursor.execute("SELECT VERSION()")
# # 使用 fetchone() 方法获取单条数据.
# data = cursor.fetchone()
# print("Database version : %s " % data)
# # 关闭数据库连接
# db.close()


# encoding=utf-8
def db_read():
    try:
        host = config.get_config_str('DATABASE', 'host')
        port = config.get_config_int('DATABASE', 'port')
        user = config.get_config_str('DATABASE', 'user')
        password = config.get_config_str('DATABASE', 'password')
        dbname = config.get_config_str('DATABASE', 'dbname')
        charset = config.get_config_str('DATABASE', 'charset')
        table = config.get_config_str('DATABASE', 'table')
        # # 获取数据库
        # db = records.Database('mysql+pymysql://root:@localhost:3306/dev01_git')
        # db_url = 'mysql+pymysql://' + user + ':' + passwd + '@' + str(host) + ':' + str(port) + '/' + db
        db_url = 'mysql+pymysql://' + user + ':' + password + '@' + host + ':' + port + '/' + dbname
        print(db_url)
        # connect = records.Database('mysql+pymysql://用户名:密码@sqlURl:sql端号/库名')
        connect = records.Database(db_url)



        # 查询
        rows = db.query('select * from lemon_user')
        id =   11
        name = 's'
        age =  '1'
        sex =  '2'
        income = 1121212
        # params = [id,name,age,sex,income]
        params = [id,name,age,sex,income]

        count=cursor.execute("insert into test_data(id,name,age,sex,income) values(%s,%s,%s,%s,%s)",params)
        print(count)
        db.commit()
        cursor.close()
        db.close()
    except Exception as e:
        print(e.message)



#

if __name__ == "__main__":
    db_canshuhua()