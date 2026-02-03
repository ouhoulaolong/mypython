import pymysql

def updata_data(args):
    #链接数据库
    con = pymysql.connect(host="localhost",user="root",password="root",db="sxt",charset="utf8")

    #获取游标对象 cursor
    cursor = con.cursor()

    #编写sql-dml
    sql = "UPDATE TEXT set age = %s where id = %s;"

    #执行sql
    cursor.execute(sql,args)

    #提交事物
    con.commit()

    #关闭cursor
    cursor.close()

    #关闭链接
    con.close()

if __name__ == '__main__':
    args = ()
    updata_data()