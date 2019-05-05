#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
created on 2019/5/5
@user: Keekuun
功能描述:
    杨辉三角
"""


def triangles(n):
    """
    杨辉三角
    :param n: 行数
    :return:
    """
    arr = [1]
    for i in range(n):
        yield arr
        arr = [sum(i) for i in zip([0] + arr, arr + [0])]


if __name__ == '__main__':
    n = int(input('请输入行数：'))
    for i in triangles(n):
        print(i)
