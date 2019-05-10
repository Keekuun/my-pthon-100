#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
created on 2019/5/10
@user: Keekuun
功能描述:
    Entry & Text部件
"""

import tkinter as tk

window = tk.Tk()
window.title('窗口标题')
window.geometry('400x200')

# 创建一个文本框用于输入，内容以“*”显示
e = tk.Entry(window, show='*')
e.pack()


# 定义点击事件
def insert_point():
    text = e.get()
    t.insert('insert', text)  # 插入到光标出


def insert_end():
    text = e.get()
    t.insert('end', text)  # 插入到最后


# 按钮
b1 = tk.Button(
    window,
    text='insert point',
    width=15,
    height=2,
    command=insert_point  # 绑定点击事件
)
b1.pack()

b2 = tk.Button(
    window,
    text='insert end',
    width=15,
    height=2,
    command=insert_end  # 绑定点击事件
)
b2.pack()

# 创建一个文本框用于显示、输入
t = tk.Text(window, height=2)
t.pack()

if __name__ == '__main__':
    # 开启窗口
    window.mainloop()
