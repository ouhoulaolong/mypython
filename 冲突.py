import threading
from threading import Thread
from time import sleep


class Account():
    def __init__(self,name,money):
        self.name = name
        self.money = money


class Drawing(Thread):
    def __init__(self,drawingnumber,account):
        Thread.__init__(self)
        self.drawingnumber = drawingnumber
        self.account = account
        self.expensetotal = 0

    def run(self):
        if self.drawingnumber > self.account.money:
            return
        sleep(1)
        self.account.money -= self.drawingnumber
        self.expensetotal += self.drawingnumber
        print(f"账户是{self.account.name},余额为{self.account.money}")
        print(f"账户是{self.account.name},总共取了{self.expensetotal}")

if __name__ == '__main__':
    a1 = Account("戴向龙",100)
    draw1 = Drawing(80,a1)
    draw2 = Drawing(80,a1)
    draw1.start()
    draw2.start()
