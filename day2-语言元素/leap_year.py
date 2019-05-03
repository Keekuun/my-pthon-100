#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
created on 2019/5/3
@user: Keekuun
功能描述:
输入年份 如果是闰年输出True 否则输出False
"""

year = int(input('请输入年份：'))
# 如果代码太长写成一行不便于阅读 可以使用\或()折行
is_leap = (year % 4 == 0
           and year % 100 != 0
           or year % 400 == 0)
print(is_leap)

if (is_leap):
    print('{}是闰年！'.format(year))
else:
    print('{}不是闰年！'.format(year))
