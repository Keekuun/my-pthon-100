#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
created on 2019/5/3
@user: Keekuun
功能描述:
输入圆的半径计算计算周长和面积。
"""

import math

radius = float(input('请输入圆的半径:'))
permimeter = 2 * math.pi * radius
area = math.pi * radius ** 2
print('半径为%.2f的圆，周长为%.2f,面积为%.2f' % (radius, permimeter, area))
