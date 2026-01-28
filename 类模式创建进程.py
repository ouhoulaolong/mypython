
from multiprocessing import Process
from time import sleep


class MyProcess(Process):
    def __init__(self,name):
        Process.__init__(self)
        self.name=name


    def run(self):
        print(f"Process:{self.name},start")
        sleep(3)
        print(f"Process:{self.name},end")



if __name__ == '__main__':
    p1 = MyProcess("p1")
    p1.start()
