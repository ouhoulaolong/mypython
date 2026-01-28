import time
from threading import Thread


def func(name):
    print(f"线程{name},start")
    for i in range(3):
        print(f"线程{name},{i}")
        time.sleep(3)
    print(f"线程{name},end")



if __name__ == '__main__':
    print("主程序，start")
    #创建进程
    t1 = Thread(target=func, args=("t1",))
    t2 = Thread(target=func, args=("t2",))

    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("主线程，end")