import pymysql
#连接数据库
con = pymysql.connect(host="localhost",port= 3306,user="root",password="root",charset=u"utf8",db = "sxt")

#获得一个和数据库交互的工具
coursor = con.cursor()


#编写sql
sql = '''
create table table_name(
id int primary key auto_increment,
name varchar(20) not null,
age int not null,
sex varchar(10) not null
)
'''

# 执行sql
coursor.execute()

#关闭数据库
coursor.close()

