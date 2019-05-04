# 练习

## 练习清单

### 1. 寻找[“水仙花数”](https://baike.baidu.com/item/%E6%B0%B4%E4%BB%99%E8%8A%B1%E6%95%B0)。
> 水仙花数（Narcissistic number）也被称为超完全数字不变数（pluperfect digital invariant, PPDI）、自恋数、自幂数、阿姆斯壮数或阿姆斯特朗数（Armstrong number），
水仙花数是指一个 3 位数，它的每个位上的数字的 3次幂之和等于它本身（例如：1^3 + 5^3+ 3^3 = 153）。

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
created on 2019/5/4
@user: Keekuun
功能描述:
    寻找水仙花数：
        水仙花数（Narcissistic number）也被称为超完全数字不变数（pluperfect digital invariant, PPDI）、自恋数、自幂数、
    阿姆斯壮数或阿姆斯特朗数（Armstrong number），水仙花数是指一个 3 位数，它的每个位上的数字的 3次幂之和等于它本身
    （例如：1^3 + 5^3+ 3^3 = 153）。
"""

num = int(input("请输入查询范围："))
while True:
    if num < 0:
        print('请输入正整数')
        num = int(input("请输入："))
    elif num < 100 or num > 999:
        print('请输入一个三位整数')
        num = int(input("请输入："))
    else:
        n = 0
        for i in range(100, num):
            hundreds = i // 100
            tens = i % 100 // 10
            ones = i % 100 % 10
            if ones ** 3 + tens ** 3 + hundreds ** 3 == i:
                print('{} = {}^3 + {}^3 + {}^3, {}是水仙花数'.format(i, ones, tens, hundreds, i))
                n += 1
        if n == 0:
            print('没有找到水仙花数')
        break
```
console结果：
```markdown
请输入查询范围：15
请输入一个三位整数
请输入：-156
请输入正整数
请输入：999
153 = 3^3 + 5^3 + 1^3, 153是水仙花数
370 = 0^3 + 7^3 + 3^3, 370是水仙花数
371 = 1^3 + 7^3 + 3^3, 371是水仙花数
407 = 7^3 + 0^3 + 4^3, 407是水仙花数
```

### 2. 寻找[“完美数”](https://baike.baidu.com/item/%E5%AE%8C%E5%85%A8%E6%95%B0/370913)。
> 完全数（Perfect number），又称完美数或完备数，是一些特殊的自然数。它所有的真因子（即除了自身以外的约数）的和（即因子函数），恰好等于它本身。如果一个数恰好等于它的因子之和，
则称该数为“完全数”。第一个完全数是6，第二个完全数是28，第三个完全数是496，后面的完全数还有8128、33550336等等。

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
created on 2019/5/4
@user: Keekuun
功能描述:
    完全数（Perfect number），又称完美数或完备数，是一些特殊的自然数。它所有的真因子（即除了自身以外的约数）的和（即因子函数），恰好等于它本身。如果一个数恰好等于它的因子之和，
    则称该数为“完全数”。第一个完全数是6，第二个完全数是28，第三个完全数是496，后面的完全数还有8128、33550336等等。
"""


num_range = input('请输入查询范围(Q/q退出)：')
while True:
    if num_range in ['Q', 'q']:
        exit()
    else:
        num_range = int(num_range)
        if num_range < 0:
            print('请输入正整数')
            num_range = input('请输入(Q/q退出)：')
        else:
            n = 0
            for num in range(1, num_range + 1):
                factors = []
                for i in range(1, int(num / 2) + 1):
                    if num % i == 0:
                        factors.append(i)
                if sum(factors) == num:
                    print('{}的真因子为{},{} = {},{}是完全数。'.format(num, factors, num, '+'.join(str(k) for k in factors), num))
                    n += 1
            if n == 0:
                print('没有找到{}范围内的完美数'.format(num_range))
                break
            break

```

console结果：
```markdown
请输入查询范围(Q/q退出)：500
6的真因子为[1, 2, 3],6 = 1+2+3,6是完全数。
28的真因子为[1, 2, 4, 7, 14],28 = 1+2+4+7+14,28是完全数。
496的真因子为[1, 2, 4, 8, 16, 31, 62, 124, 248],496 = 1+2+4+8+16+31+62+124+248,496是完全数。
```

### 3. [“百鸡百钱”](https://baike.baidu.com/item/%E7%99%BE%E9%B8%A1%E7%99%BE%E9%92%B1/5857320)问题。
> 我国古代数学家张丘建在《算经》一书中提出的数学问题：鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
created on 2019/5/4
@user: Keekuun
功能描述:
     “百鸡百钱”问题: 我国古代数学家张丘建在《算经》一书中提出的数学问题：鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？
"""

rooster = 5
hen = 3
chick = 1 / 3

for i in range(1, 100):
    for j in range(1, 100):
        for k in range(1, 100):
            if i + j + k == 100 and i * rooster + j * hen + k * chick == 100:
                print('100钱买100只鸡：公鸡%d只，母鸡%d只，小鸡%d只' % (i, j, k))
                exit()
```

console结果：
```markdown
100钱买100只鸡：公鸡4只，母鸡18只，小鸡78只
```

### 4. 生成[“斐波拉切数列”](https://baike.baidu.com/item/%E6%96%90%E6%B3%A2%E9%82%A3%E5%A5%91%E6%95%B0%E5%88%97/99145)。
> 斐波那契数列（Fibonacci sequence），又称黄金分割数列、因数学家列昂纳多·斐波那契（Leonardoda Fibonacci）以兔子繁殖为例子而引入，故又称为“兔子数列”，
指的是这样一个数列：1、1、2、3、5、8、13、21、34、……在数学上，斐波纳契数列以如下被以递推的方法定义：F(1)=1，F(2)=1, F(n)=F(n-1)+F(n-2)（n>=3，n∈N*）
在现代物理、准晶体结构、化学等领域，斐波纳契数列都有直接的应用，为此，美国数学会从1963年起出版了以《斐波纳契数列季刊》为名的一份数学杂志，用于专门刊载这方面的研究成果。

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
created on 2019/5/4
@user: Keekuun
功能描述:
    斐波那契数列（Fibonacci sequence），又称黄金分割数列、因数学家列昂纳多·斐波那契（Leonardoda Fibonacci）以兔子繁殖为例子而引入，故又称为“兔子数列”，
指的是这样一个数列：1、1、2、3、5、8、13、21、34、……在数学上，斐波纳契数列以如下被以递推的方法定义：F(1)=1，F(2)=1, F(n)=F(n-1)+F(n-2)（n>=3，n∈N*）
"""

num = int(input('输入一个正整数，我将输出对应个数的斐波那契数列：'))


def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


arr = []
for i in range(1, num + 1):
    arr.append(fib(i))
print(arr)

```

console结果：
```markdown
输入一个正整数，我将输出对应个数的斐波那契数列：10
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
```

### 5. 五人分鱼问题。
> 问题 : 有五个人捕获了足够数量的鱼,第二天早上,五个人依次起来。
        第一个人将于均分为五份后多了一条鱼,将其扔掉后,拿走一份；
        第二个人将剩下的鱼均分为五份后又多了一条鱼,将其扔掉后,拿走一份；
        第三个人...
        第四个人...
        第五个人...
     问：鱼几何？
     
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
created on 2019/5/4
@user: Keekuun
功能描述:
    问题 : 有五个人捕获了足够数量的鱼,第二天早上,五个人依次起来。                   m
        第一个人将鱼均分为五份后多了一条鱼,将其扔掉后,拿走一份；                   n = (m - 1) / 5 * 4
        第二个人将剩下的鱼均分为五份后又多了一条鱼,将其扔掉后,拿走一份；            p = (n - 1) / 5 * 4
        第三个人...                                                        q = (p - 1) / 5 * 4
        第四个人...
        第五个人...
        问：鱼几何？
"""

fish = 6

while True:
    rest = fish
    is_ok = True
    for i in range(5):
        if (rest - 1) % 5 == 0:
            rest = (rest - 1) / 5 * 4
        else:
            is_ok = False
            break
    if is_ok:
        print('共捕鱼至少%d条' % fish)
        break
    fish += 1

```
console结果
```markdown
共捕鱼至少3121条
```

### 6. Craps赌博游戏。
> 玩家掷两个骰子，点数为1到6，如果点数和为7或11，则玩家胜；如果点数和为2、3或12，则玩家输；如果和为其它点数，则记录第一次的点数和，然后继续掷骰，
直至点数和等於第一次掷出的点数和，则玩家胜，如果在这之前掷出了点数和为7，则玩家输。

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
created on 2019/5/4
@user: Keekuun
功能描述:
    Craps赌博游戏:
        玩家掷两个骰子，点数为1到6，如果点数和为7或11，则玩家胜；如果点数和为2、3或12，则玩家输；如果和为其它点数，则记录第一次的点数和，然后继续掷骰，
    直至点数和等於第一次掷出的点数和，则玩家胜，如果在这之前掷出了点数和为7，则玩家输。
"""

from random import randint

a = randint(1, 6)
b = randint(1, 6)
s = a + b
player = True
print(a, b)
while True:
    if s in [7, 11]:
        print('玩家胜！')
        break
    if s in [2, 3, 12]:
        player = False
        print('玩家败！')
        break
    else:
        print('继续掷骰')
        player = False
        b = randint(1, 6)
        s = a + b
        print(a, b)
        if s == 7:
            player = False
            print('玩家败！')
            break
        if b == a:
            player = True
    if player:
        print('玩家胜！')
        break

```

console结果：
```markdown
4 2
继续掷骰
4 1
继续掷骰
4 5
继续掷骰
4 1
继续掷骰
4 6
继续掷骰
4 5
继续掷骰
4 5
继续掷骰
4 6
继续掷骰
4 2
继续掷骰
4 4
玩家胜！
```