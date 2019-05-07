#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
created on 2019/5/7
@user: Keekuun
功能描述：
    classmethod类方法
"""

from time import time, localtime, sleep


class Clock:
    """数字时钟"""

    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    # 类方法:类方法的第一个参数约定名为cls,代表当前类相关的信息的对象
    @classmethod
    def now(cls):
        ctime = localtime(time())
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)

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

    def show(self):
        """显示时间"""
        return '%02d:%02d:%02d' % \
               (self._hour, self._minute, self._second)

    # 优化对象输出，定义输出内容
    def __str__(self):

        """显示时间"""
        return '%02d:%02d:%02d' % \
               (self._hour, self._minute, self._second)


def run():
    # 通过类方法创建对象并获取系统时间
    clock = Clock.now()
    while True:
        print(clock)
        print(clock.show())
        sleep(1)
        clock.run()


if __name__ == '__main__':
    run()
