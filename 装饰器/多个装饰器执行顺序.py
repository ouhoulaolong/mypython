import time

def mylog(func):
    print("mylog,start")
    def infunc():
        print("日志记录 start")
        func()
        print("日志记录 end")
    print("mylog,end")
    return infunc




def cost_time(func):
    print("cost_time   start")
    def infunc():
        print("开始计时")
        start = time.time()
        func()
        end = time.time()
        print(f"消耗时间{end-start}")
    print("cost_time   end")
    return infunc

@mylog
@cost_time
def fun2():
    print("fun2,start")
    time.sleep(3)
    print("fun2,end")


fun2()