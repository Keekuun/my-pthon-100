#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
created on 2019/5/3
@user: Keekuun
功能描述:
    掷骰子决定做什么事情
"""

from random import randint

# get random number 1-6
face = randint(1, 6)
print(face)

if face == 1:
    res = 'lol'
elif face == 2:
    res = 'lol'
elif face == 3:
    res = 'python'
elif face == 4:
    res = 'spider!'
elif face == 5:
    res = 'what you like!'
else:
    res = 'nothing!'

print('play ' + res)
