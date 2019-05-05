#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
created on 2019/5/5
@user: Keekuun
功能描述:
    练习1：在屏幕上显示跑马灯文字
"""

import os
import time


def main():
    content = '人生苦短，我用Python…………'
    while True:
        # 清理屏幕上的输出
        os.system('cls')  # os.system('clear')
        print(content)
        # 休眠200毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]


if __name__ == '__main__':
    main()

