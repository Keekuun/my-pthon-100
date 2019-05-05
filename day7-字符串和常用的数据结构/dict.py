#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
created on 2019/5/5
@user: Keekuun
功能描述:
    字典的操作
"""

def main():
    scores = {'math': 95, 'PE': 78, 'EN': 82}

    # 通过键可以获取字典中对应的值
    print(scores['math'])
    print(scores['PE'])

    # 对字典进行遍历(遍历的其实是键再通过键取对应的值)
    for elem in scores:
        print('%s\t--->\t%d' % (elem, scores[elem]))

    # 更新字典中的元素
    scores['math'] = 65
    scores['PE'] = 71
    scores.update(art=67, CH=85)
    print(scores)

    if 'PE' in scores:
        print(scores['PE'])
    print(scores.get('PE'))

    # get方法也是通过键获取对应的值但是可以设置默认值
    print(scores.get('EN', 60))

    # 删除字典中的元素
    print(scores.popitem())
    print(scores.popitem())
    print(scores.pop('EN', 100))

    # 清空字典
    scores.clear()
    print(scores)


if __name__ == '__main__':
    main()