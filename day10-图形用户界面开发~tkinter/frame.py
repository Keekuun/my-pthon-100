#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
created on 2019/5/10
@user: Keekuun
功能描述:
    Frame部件
"""

import tkinter as tk

root = tk.Tk()
root.geometry('400x200')

# 定义一个label显示
tk.Label(root, text='人生苦短，我用Python!').pack()

# 创建一个'frame'
frm = tk.Frame(root)
frm.pack()

# 在`frm`中再创建两个'frame'，即大容器包小容器
frm_left = tk.Frame(frm)
frm_right = tk.Frame(frm)

# 设置小容器的位置
frm_left.pack(side='left')
frm_right.pack(side='right')

# 显示的内容
tk.Label(frm_left, text='人生苦短').pack()
tk.Label(frm_right, text='hello world').pack()
tk.Label(frm_left, text='我用Python').pack()

if __name__ == '__main__':
    root.mainloop()