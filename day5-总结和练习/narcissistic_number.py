#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
created on 2019/5/4
@user: Keekuun
功能描述:
    寻找水仙花数：
        水仙花数（Narcissistic number）也被称为超完全数字不变数（pluperfect digital invariant, PPDI）、自恋数、自幂数、
    阿姆斯壮数或阿姆斯特朗数（Armstrong number），水仙花数是指一个 3 位数，它的每个位上的数字的 3次幂之和等于它本身
    （例如：1^3 + 5^3+ 3^3 = 153）。
"""

num = int(input("请输入查询范围："))
while True:
    if num < 0:
        print('请输入正整数')
        num = int(input("请输入："))
    elif num < 100 or num > 999:
        print('请输入一个三位整数')
        num = int(input("请输入："))
    else:
        n = 0
        for i in range(100, num):
            hundreds = i // 100
            tens = i % 100 // 10
            ones = i % 100 % 10
            if ones ** 3 + tens ** 3 + hundreds ** 3 == i:
                print('{} = {}^3 + {}^3 + {}^3, {}是水仙花数'.format(i, ones, tens, hundreds, i))
                n += 1
        if n == 0:
            print('没有找到水仙花数')
        break
