#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
created on 2019/5/3
@user: Keekuun
功能描述:
将华氏温度转换为摄氏温度
F = 1.8C + 32
"""

f = float(input('请输入华氏温度：'))
c = (f - 32) / 1.8

print('{}华氏温度 = {}摄氏温度'.format(f, c))
print('%.1f华氏温度 = %.1f摄氏温度' % (f, c))

