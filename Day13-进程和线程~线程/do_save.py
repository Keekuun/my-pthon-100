#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
created on 2019/5/11
@user: Keekuun
功能描述
"""

import time, threading

money = 0

def save(n):
    global money
    money = money + n
    money = money - n

def run(n):
    for i in range(100000000):
        save(n)


if __name__ == '__main__':
    t1 = threading.Thread(target=run, args=(5,))
    t2 = threading.Thread(target=run, args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(money)