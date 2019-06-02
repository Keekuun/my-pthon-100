#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
created on 2019/5/11
@user: Keekuun
功能描述
    启动大量进程---进程池Pool
"""

from multiprocessing import Pool
import os, time, random


def long_time_task(name):
    print('Run task %s(%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 5)
    end = time.time()
    print('Task %s runs %.2f seconds.' % (name, (end - start)))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool()
    for i in range(6):
        # p.apply(long_time_task, args=(i,))
        p.apply_async(long_time_task, args=(i,))  # 异步
    print('Waiting for all subprocess done...')
    p.close()
    p.join()
    print('All subprocess done.')
