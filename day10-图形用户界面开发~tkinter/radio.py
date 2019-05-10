#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
created on 2019/5/10
@user: Keekuun
功能描述:
    Radiobutton部件
"""

import tkinter as tk

root = tk.Tk()

root.title('list box')
root.geometry('400x200')

l = tk.Label(root, bg='yellow', width=20, text='empty')
l.pack()


def print_selection():
    l.config(text='you have selected ' + radiovar.get())


item = [('option A', 'A'), ('option B', 'B'), ('option C', 'C'),
        ('option D', 'D'), ('option E', 'E')]
radiovar = tk.StringVar()
for text, value in item:
    tk.Radiobutton(
        root,
        text=text,
        value=value,
        variable=radiovar,
        command=print_selection
    ).pack()

radiovar.set('B')

if __name__ == '__main__':
    root.mainloop()