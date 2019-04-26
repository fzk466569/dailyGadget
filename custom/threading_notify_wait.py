#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  18:45


import threading


class ZSThead(threading.Thread):
    def __init__(self, name, cond):
        super(ZSThead, self).__init__()
        self.name = name
        self.cond = cond
        self.data = list(range(0, 100, 2))

    def run(self):
        # 必须先调用with self.cond，才能使用wait()、notify()方法
        while self.data:
            with self.cond:
                print(self.data.pop(0))
                self.cond.notify()
                self.cond.wait()


class LSThread(threading.Thread):
    def __init__(self, name, cond):
        super(LSThread, self).__init__()
        self.name = name
        self.cond = cond
        self.data = list(range(1, 101, 2))

    def run(self):
        while self.data:
            with self.cond:
                self.cond.wait()
                print(self.data.pop(0))
                self.cond.notify()


if __name__ == '__main__':
    cond = threading.Condition()
    zs = ZSThead("张三", cond)
    ls = LSThread("李四", cond)

    # 启动顺序很重要，必须先启动李四，让他在那里等待着，
    # 因为先启动张三时，他说了话就发出了通知，但是当时李四的进程还没有启动，
    # 并且condition外面的大锁也没有释放，李四也没法获取self.cond这把大锁
    # condition有两层锁，一把底层锁在线程调用了wait()方法就会释放
    # 每次调用wait()方法后，都会创建一把锁放进condition的双向队列中，等待notify()方法的唤醒
    ls.start()
    zs.start()
