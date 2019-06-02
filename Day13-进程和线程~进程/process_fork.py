#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
created on 2019/5/11
@user: Keekuun
功能描述
    开启多进程下载文件
"""

import os

print('Process (%s) start...' % os.getpid())
# Only works on Unix/Linux/Mac:
pid = os.fork()
if pid == 0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
