#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
created on 2019/5/5
@user: Keekuun
功能描述:
    设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成。
"""

import random


def generate_code(code_len=4):
    """
    生成指定长度的验证码
    :param code_len: 验证码的长度(默认4个字符)
    :return: 由大小写英文字母和数字构成的随机验证码
    """
    word = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    word_len = len(word) - 1
    code = ''

    for i in range(code_len):
        index = random.randint(0, word_len)
        code += word[index]
    return code


if __name__ == '__main__':
    print(generate_code(4))
