#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
created on 2019/5/4
@user: Keekuun
功能描述:
    问题 : 有五个人捕获了足够数量的鱼,第二天早上,五个人依次起来。                   m
        第一个人将鱼均分为五份后多了一条鱼,将其扔掉后,拿走一份；                   n = (m - 1) / 5 * 4
        第二个人将剩下的鱼均分为五份后又多了一条鱼,将其扔掉后,拿走一份；            p = (n - 1) / 5 * 4
        第三个人...                                                        q = (p - 1) / 5 * 4
        第四个人...
        第五个人...
        问：鱼几何？
"""

fish = 6

while True:
    rest = fish
    is_ok = True
    for i in range(5):
        if (rest - 1) % 5 == 0:
            rest = (rest - 1) / 5 * 4
        else:
            is_ok = False
            break
    if is_ok:
        print('共捕鱼至少%d条' % fish)
        break
    fish += 1
