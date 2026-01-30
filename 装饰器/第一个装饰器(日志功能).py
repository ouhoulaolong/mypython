

#开闭原则

def outer(func):
    def inner(*args,**kwargs):
        func(*args,**kwargs)
        print("日志记录......")
    return inner


def fun1():
    print("调用方法1")


def fun2(a,b):
    print("调用方法2",a,b)

fun1 = outer(fun1)
fun2 = outer(fun2)

fun1()
fun2(100,200)