#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
created on 2019/5/4
@user: Keekuun
功能描述:
    Craps赌博游戏:
        玩家掷两个骰子，点数为1到6，如果点数和为7或11，则玩家胜；如果点数和为2、3或12，则玩家输；如果和为其它点数，则记录第一次的点数和，然后继续掷骰，
    直至点数和等於第一次掷出的点数和，则玩家胜，如果在这之前掷出了点数和为7，则玩家输。
"""

from random import randint

a = randint(1, 6)
b = randint(1, 6)
s = a + b
player = True
print(a, b)
while True:
    if s in [7, 11]:
        print('玩家胜！')
        break
    if s in [2, 3, 12]:
        player = False
        print('玩家败！')
        break
    else:
        print('继续掷骰')
        player = False
        b = randint(1, 6)
        s = a + b
        print(a, b)
        if s == 7:
            player = False
            print('玩家败！')
            break
        if b == a:
            player = True
    if player:
        print('玩家胜！')
        break
