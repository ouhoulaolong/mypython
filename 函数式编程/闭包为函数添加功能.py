#本次内容为装饰器的基础


def outfunc(func):
    def infunc():
        print("日志功能....")
        func()
    return infunc



def func1():
    print("使用功能1")


func1 = outfunc(func1)
func1()