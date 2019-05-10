#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
created on 2019/5/10
@user: Keekuun
功能描述:
    messagebox部件
"""
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

root.geometry('400x200')


def click():
    tk.messagebox.showinfo(title='Hello World!', message='人生苦短，我用Python!')


tk.Button(root, text='Say Hi', command=click).pack()

if __name__ == '__main__':
    root.mainloop()
    print(tk.messagebox.askquestion())  # 返回yes和no
    print(tk.messagebox.askokcancel())  # 返回true和false
    print(tk.messagebox.askyesno())  # 返回true和false
    print(tk.messagebox.askretrycancel())  # 返回true和false