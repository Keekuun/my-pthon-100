#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
created on 2019/5/10
@user: Keekuun
功能描述:
    Listbox部件
"""
import tkinter as tk

root = tk.Tk()

root.title('list box')
root.geometry('400x200')

# 创建一个label用于显示
labelvar = tk.StringVar(value='人生苦短，我用Python')
l = tk.Label(root, bg='green', textvariable=labelvar)
l.pack()


# 定义点击事件
def print_selection():
    # 获取当前选中的文本
    curselection = lb.get(lb.curselection())
    # 显示当前选中的文本
    labelvar.set(curselection)


# 按钮绑定事件
b = tk.Button(root, text='print selection', command=print_selection)
b.pack()

listvar = tk.StringVar(value=['list box', 'hello world', '人生苦短，我用Python'])
# list box选择框
lb = tk.Listbox(root, listvariable=listvar)
lb.pack()

if __name__ == '__main__':
    root.mainloop()