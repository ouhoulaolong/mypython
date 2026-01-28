import threading
import time


class MyThread(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        print(f"线程{self.name},start")
        for i in range(3):
            time.sleep(3)
            print(f"线程{self.name},{i}")
        print(f"线程{self.name},end")

if __name__=="__main__":
    print(f"主线程,start")
    t1 = MyThread("t1")
    t1.daemon = True
    t1.start()

    print(f"主线程,end")