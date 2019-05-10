#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
created on 2019/5/10
@user: Keekuun
功能描述:
    Scale部件
"""

import tkinter as tk

root = tk.Tk()
root.title('Scale')
root.geometry('400x200')

l = tk.Label(root, bg='green', text='hello')
l.pack()


def scale(v):
    l.config(text='you have drag me to ' + v)


s = tk.Scale(
    root,
    label='drag me',
    from_=1,
    to=15,
    orient=tk.HORIZONTAL,
    length=400,
    showvalue=1,
    tickinterval=2,
    resolution=0.01,
    command=scale
).pack()


if __name__ == '__main__':
    root.mainloop()
