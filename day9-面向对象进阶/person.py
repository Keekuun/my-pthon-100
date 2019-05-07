#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
created on 2019/5/7
@user: Keekuun
功能描述:
    getter和setter方法
"""


class Person:
    """
     @property:把一个getter方法变成属性(只读)
     @age.setter:把一个setter方法变成属性(读写)
    """

    # 限定Person对象只能绑定_name, _age和_gender属性
    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 访问器 - getter方法
    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    # 修改器 - getter方法
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s岁时%s正在玩王者荣耀' % (self._age, self._name))
        else:
            print('%s岁时%s正在玩英雄联盟' % (self._age, self._name))


def run():
    person = Person('UZI', 20)
    person.play()
    person.age = 12
    person.play()
    # AttributeError: can't set attribute
    # person.name = 'Little Dog'


if __name__ == '__main__':
    run()
