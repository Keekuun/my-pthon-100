#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
created on 2019/5/4
@user: Keekuun
功能描述:
    完全数（Perfect number），又称完美数或完备数，是一些特殊的自然数。它所有的真因子（即除了自身以外的约数）的和（即因子函数），恰好等于它本身。如果一个数恰好等于它的因子之和，
    则称该数为“完全数”。第一个完全数是6，第二个完全数是28，第三个完全数是496，后面的完全数还有8128、33550336等等。
"""


num_range = input('请输入查询范围(Q/q退出)：')
while True:
    if num_range in ['Q', 'q']:
        exit()
    else:
        num_range = int(num_range)
        if num_range < 0:
            print('请输入正整数')
            num_range = input('请输入(Q/q退出)：')
        else:
            n = 0
            for num in range(1, num_range + 1):
                factors = []
                for i in range(1, int(num / 2) + 1):
                    if num % i == 0:
                        factors.append(i)
                if sum(factors) == num:
                    print('{}的真因子为{},{} = {},{}是完全数。'.format(num, factors, num, '+'.join(str(k) for k in factors), num))
                    n += 1
            if n == 0:
                print('没有找到{}范围内的完美数'.format(num_range))
                break
            break

