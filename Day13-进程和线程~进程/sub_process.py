#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
created on 2019/5/11
@user: Keekuun
功能描述:
    子进程
"""

import subprocess

print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('gbk'))
print('Exit code:', p.returncode)
