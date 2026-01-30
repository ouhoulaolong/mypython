def mylog(type):
    def decorator(func):
        def infunc(*args,**kargs):
            if type=="文件":
                print("文件中：日志记录")
            else:
                print("控制台：日志记录")
            return func(*args,**kargs)
        return infunc
    return decorator

@mylog("文件")
def fun2(a,b):
    print("使用功能2",a,b)

if __name__ == "__main__":
    fun2(100,200)