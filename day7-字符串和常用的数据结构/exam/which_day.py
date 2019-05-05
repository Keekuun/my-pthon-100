#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
created on 2019/5/5
@user: Keekuun
功能描述:
    计算指定的年月日是这一年的第几天
"""


def is_leap_year(year):
    """
    判断指定的年份是不是闰年
    :param year: 年份
    :return: 闰年返回True平年返回False
    """
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def which_day(year, month, day):
    # 作为索引：True -> 1; False -> 0
    days_of_month = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ][is_leap_year(year)]

    total = 0
    for index in range(month - 1):
        total += days_of_month[index]
    return total


if __name__ == '__main__':
    print(which_day(2019, 5, 6))
    print(which_day(1981, 12, 31))
    print(which_day(2018, 1, 1))
    print(which_day(2016, 3, 1))
