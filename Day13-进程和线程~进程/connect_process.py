#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
created on 2019/5/11
@user: Keekuun
功能描述
    进程间通信
"""

from multiprocessing import Process, Queue
import os, time, random


# 写数据进程执行的任务
def line(q):
    print('欢迎来到召唤师峡谷（战场编号: %s）' % os.getpid())

    for hero in ['蛮', '易', '信']:
        print('%s 上线了' % hero)
        q.put(hero)
        time.sleep(random.random())


# 读数据进程执行的任务
def gank(q):
    print('Gank即将开始（Gank编号: %s）' % os.getpid())
    while True:
        hero = q.get(True)
        print('%s 来Gank了!.' % hero)


if __name__ == '__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pl = Process(target=line, args=(q,))
    pg = Process(target=gank, args=(q,))

    # 启动子进程line
    pl.start()

    # 启动子进程gank
    pg.start()

    # 等待line结束
    pl.join()

    # gank进程里是死循环，无法等待其结束，只能强行终止:
    pg.terminate()
