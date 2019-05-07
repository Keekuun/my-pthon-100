#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
created on 2019/5/7
@user: Keekuun
功能描述:
    类的继承
"""


class Person:
    """人"""

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # getter(只读属性)
    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    # setter(读写属性)
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        print('%s正在愉快的玩耍.' % self._name)

    def watch_av(self):
        if self._age >= 18:
            print('%s正在观看爱情动作片.' % self._name)
        else:
            print('%s只能观看《天线宝宝》.' % self._name)


# Student继承了Person
class Student(Person):
    """学生"""

    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self, course):
        print('%s的%s正在学习%s.' % (self._grade, self._name, course))


# Teacher继承了Person
class Teacher(Person):
    """老师"""

    def __init__(self, name, age, title):
        super().__init__(name, age)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def teach(self, course):
        print('%s%s正在讲%s.' % (self._name, self._title, course))


def run():
    stu = Student('小明', 15, '初三')
    stu.study('数学')
    stu.watch_av()
    t = Teacher('秦少', 25, '小白脸')
    t.teach('Python')
    t.watch_av()


if __name__ == '__main__':
    run()
