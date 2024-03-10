# 多线程竞争资源
# 多个线程竞争一个资源 - 保护临界资源 - 锁（Lock/RLock）
# 多个线程竞争多个资源（线程数>资源数） - 信号量（Semaphore）
# 多个线程的调度 - 暂停线程执行/唤醒等待中的线程 - Condition

from time import sleep
from random import randint
from concurrent.futures import ThreadPoolExecutor
import threading


class Account:
    def __init__(self,balance = 0):
        self.balance = balance
        self.lock = threading.RLock()
        self.condition = threading.Condition(self.lock)

    def withdraw(self,money):
        with self.condition:
            # before_balance = self.balance
            while self.balance < money: # 账户不足以扣除，则需要进入阻塞
                self.condition.wait()
            new_balance = self.balance - money
            sleep(0.01)
            self.balance = new_balance
            # print(threading.current_thread().name, ':', f'withdraw {money}',
            #       f'before : {before_balance} =====> after : {self.balance}')
            self.condition.notify_all()

    def deposit(self,money):
        with self.condition:
            # before_balance = self.balance
            new_balance = self.balance + money
            sleep(0.01)
            self.balance = new_balance
            # print(threading.current_thread().name, ':', f'deposit {money}',
            #       f'before : {before_balance} ====> after : {self.balance}')
            self.condition.notify_all() # 通知唤醒其他线程

def add_money(account):
    while True:
        with account.condition:
            before_balance = account.balance
            money = randint(5,10)
            account.deposit(money)
            print(threading.current_thread().name,':',f'deposit {money}',
                  f'before : {before_balance} ====> after : {account.balance}')
        sleep(0.5)

def sub_money(account):
    while True:
        with account.condition:
            before_balance = account.balance
            money = randint(10,30)
            account.withdraw(money)
            print(threading.current_thread().name,':',f'withdraw {money}',
                  f'before : {before_balance} =====> after : {account.balance}')
        sleep(1)

def main():
    account = Account()
    with ThreadPoolExecutor(max_workers=15) as pool:
        for _ in range(5):
            pool.submit(add_money,account)
        for _ in range(10):
            pool.submit(sub_money,account)

if __name__ == '__main__':
    main()