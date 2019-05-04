#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
created on 2019/5/4
@user: Keekuun
功能描述:
    斐波那契数列（Fibonacci sequence），又称黄金分割数列、因数学家列昂纳多·斐波那契（Leonardoda Fibonacci）以兔子繁殖为例子而引入，故又称为“兔子数列”，
指的是这样一个数列：1、1、2、3、5、8、13、21、34、……在数学上，斐波纳契数列以如下被以递推的方法定义：F(1)=1，F(2)=1, F(n)=F(n-1)+F(n-2)（n>=3，n∈N*）
"""

num = int(input('输入一个正整数，我将输出对应个数的斐波那契数列：'))


def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


arr = []
for i in range(1, num + 1):
    arr.append(fib(i))
print(arr)
