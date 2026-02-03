import pymysql
#连接数据库
con = pymysql.connect(host="localhost",port= 3306,user="root",password="root",charset=u"utf8")

#获得一个和数据库交互的工具
coursor = con.cursor()


#编写sql
sql = '''
create database sxt default character set = "utf8mb4"
'''

# 执行sql
coursor.execute()

#关闭数据库
coursor.close()

