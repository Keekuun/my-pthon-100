#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
created on 2019/5/6
@user: Keekuun
功能描述:
    定义一个类描述数字时钟
"""

import time


class Clock:
    """数字时钟"""

    def __init__(self, hour=0, minute=0, second=0):
        """初始化方法

        :param hour: 时
        :param minute: 分
        :param second: 秒
        """
        self._hour = hour
        self._minute = minute
        self._second = second

    def run(self):
        """走字"""
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def __str__(self):
        """显示时间"""
        return '%02d:%02d:%02d' % \
               (self._hour, self._minute, self._second)


def main():
    clock = Clock(21, 53, 00)
    while True:
        print(clock)
        time.sleep(1)
        clock.run()


if __name__ == '__main__':
    main()
