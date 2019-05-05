#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
created on 2019/5/5
@user: Keekuun
功能描述:
    设计一个函数返回传入的列表中最大和第二大的元素的值。
"""


def max2(x):
    m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
    for index in range(2, len(x)):
        if x[index] > m1:
            m2 = m1
            m1 = x[index]
        elif x[index] > m2:
            m2 = x[index]
    return m1, m2


if __name__ == '__main__':
    x = [31, 25, 49, 99, 5, 6]
    print(max2(x))
