#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
created on 2019/5/3
@user: Keekuun
功能描述:
    打印各种三角形图案

*
**
***
****
*****

    *
   **
  ***
 ****
*****

    *
   ***
  *****
 *******
*********
"""

row = int(input('请输入行数：'))
for i in range(row):
    for j in range(i + 1):
        print('*', end=' ')
    print()

print('-' * 100)
for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ', end=' ')
        else:
            print('*', end=' ')
    print()

print('-' * 100)
for i in range(row):
    for _ in range(row - i - 1):
        print(' ', end='')
    for _ in range(2 * i + 1):
        print('*', end='')
    print()
