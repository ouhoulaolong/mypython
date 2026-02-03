from mimetypes import init

import pymysql
'''
在python的pymysql模块，如果需要执行DML语句，需要提交事务，con.commit()
'''
def addone():
    #链接数据库
    con = pymysql.connect(host="localhost",user="root",password="root",db="sxt",charset="utf8")

    #获取操作数据的对象 cursor
    cursor = con.cursor

    #编写sql-dml
    sql = "INSERT INTO TEXT VALUES (0,%S,%S,%S);"
    args = ("刘备",22,"男")

    #执行sql
    cursor.execute(sql,args)

    #提交事物
    con.commit()

    #关闭cursor
    cursor.close()

    #关闭链接
    con.close()

def addmany():
    #链接数据库
    con = pymysql.connect(host="localhost",user="root",password="root",db="sxt",charset="utf8")

    #获取操作数据的对象 cursor
    cursor = con.cursor

    #编写sql-dml
    sql = "INSERT INTO TEXT VALUES (0,%S,%S,%S);"
    args = (("刘备",22,"男"),("孙权",23,"男"))

    #执行sql
    cursor.executemany(sql,args)

    #提交事物
    con.commit()

    #关闭cursor
    cursor.close()

    #关闭链接
    con.close()

if __name__ == '__main__':
    addmany()