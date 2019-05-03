#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
created on 2019/5/3
@user: Keekuun
功能描述：
    百分制成绩转等级制成绩
    90分以上          --> A
    80分~89分         --> B
    70分~79分	      --> C
    60分~69分         --> D
    60分以下          --> E
"""

score = float(input('请输入成绩： '))

if score >= 90:
    rank = 'A'
elif score >= 80:
    rank = 'B'
elif score >= 70:
    rank = 'C'
elif score >= 60:
    rank = 'D'
else:
    rank = 'E'
print('对应的等级是:', rank)
