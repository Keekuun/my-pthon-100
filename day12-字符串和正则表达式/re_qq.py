#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
created on 2019/5/11
@user: Keekuun
功能描述:
    验证输入用户名和QQ号是否有效并给出对应的提示信息
    要求：用户名必须由字母、数字或下划线构成且长度在6~20个字符之间，QQ号是5~12的数字且首位不能为0
"""

import re


def main():
    username = input('请输入用户名：')
    qq = input('请输入QQ号：')

    '''
        match函数的第一个参数是正则表达式字符串或正则表达式对象
        第二个参数是要跟正则表达式做匹配的字符串对象
    '''
    re_name = re.match(r'^\w{6,20}$', username)
    re_qq = re.match(r'^[1-9]\d{4,11}$', qq)

    if not re_name:
        print('请输入有效的用户名！')
    if not re_qq:
        print('请输入有效的QQ号！')


if __name__ == '__main__':
    main()
