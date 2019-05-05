#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
created on 2019/5/5
@user: Keekuun
功能描述:
    元组的操作
"""

def main():
    # 定义元组
    t = ('秦少', 38, True, '月上')
    print(t)

    # 获取元组中的元素
    print(t[0])
    print(t[3])

    # 遍历元组中的值
    for member in t:
        print(member)

    # 重新给元组赋值
    # t[0] = '王大锤'  # TypeError

    # 变量t重新引用了新的元组原来的元组将被垃圾回收
    t = ('王大锤', 20, True, '云南昆明')
    print(t)

    # 将元组转换成列表
    person = list(t)
    print(person)

    # 列表是可以修改它的元素的
    person[0] = '李小龙'
    person[1] = 25
    print(person)

    # 将列表转换成元组
    fruits_list = ['apple', 'banana', 'orange']
    fruits_tuple = tuple(fruits_list)
    print(fruits_tuple)


if __name__ == '__main__':
    main()
