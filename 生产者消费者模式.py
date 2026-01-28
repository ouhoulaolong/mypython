import threading
from queue import Queue
from time import sleep


def producer():
    num  = 1
    while True:
        if queue.qsize()<5:
            print(f"生产{num}号，大馒头")
            queue.put(f"大馒头，{num}号")
            num +=1
        else:
            print("馒头框放满了，等待消费者消费")
            sleep(1)
def consumer():
    while True:
        print(f"获取了{queue.get()}")
        sleep(1)



if __name__=="__main__":
    queue = Queue()
    t1 = threading.Thread(target=producer)
    t2 = threading.Thread(target=consumer)
    t1.start()
    t2.start()