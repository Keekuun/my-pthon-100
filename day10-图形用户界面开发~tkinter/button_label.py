#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
created on 2019/5/10
@user: Keekuun
功能描述:
    Label & Button部件
"""
import tkinter as tk

window = tk.Tk()
window.title('窗口标题')
window.geometry('400x200')

# 定义变量并设置默认值
text = tk.StringVar(value='hello')

# 文本标签
label = tk.Label(
    window,
    textvariable=text,   # 使用 textvariable(变量) 替换 text(定值),
    bg='#ccc',           # 背景色
    font=('Arial', 12),  # 字体及大小
    width=15,            # 标签宽度
    height=2             # 标签高度
)

label.pack()


# 判断点击事件，切换文本
flag = True


# 定义点击事件
def click():
    global flag
    if flag:
        text.set('you click me!')
        flag = False
    else:
        text.set('hello world!')
        flag = True


# 按钮
button = tk.Button(
    window,
    text='click',
    bg='#f60',
    font=('Arial', 12),
    width=15,
    height=2,
    command=click   # 绑定点击事件
)
button.pack()

# 开启窗口
if __name__ == '__main__':
    window.mainloop()