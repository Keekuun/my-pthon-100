#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
created on 2019/5/7
@user: Keekuun
功能描述:
    多态
"""

from abc import ABCMeta, abstractmethod


class Pet(metaclass=ABCMeta):
    """宠物"""

    def __init__(self, nickname):
        self._nickname = nickname

    # 通过abc模块的ABCMeta元类和abstractmethod包装器来达到抽象类的效果
    @abstractmethod
    def make_voice(self):
        """发出声音"""
        pass


class Dog(Pet):
    """狗"""

    def make_voice(self):
        print('%s: 汪汪汪...' % self._nickname)


class Cat(Pet):
    """猫"""

    def make_voice(self):
        print('%s: 我们一起学猫叫，一起喵喵喵^_^' % self._nickname)


def run():
    pets = [Dog('旺财'), Cat('橘猫'), Dog('大黄')]
    for pet in pets:
        pet.make_voice()


if __name__ == '__main__':
    run()
