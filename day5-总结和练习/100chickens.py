#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
created on 2019/5/4
@user: Keekuun
功能描述:
     “百鸡百钱”问题: 我国古代数学家张丘建在《算经》一书中提出的数学问题：鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？
"""

rooster = 5
hen = 3
chick = 1 / 3

for i in range(1, 100):
    for j in range(1, 100):
        for k in range(1, 100):
            if i + j + k == 100 and i * rooster + j * hen + k * chick == 100:
                print('100钱买100只鸡：公鸡%d只，母鸡%d只，小鸡%d只' % (i, j, k))
                exit()
