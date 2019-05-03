# Day03 - 分支结构

## 分支结构的应用场景

迄今为止，我们写的Python代码都是一条一条语句顺序执行，这种结构的代码我们称之为顺序结构。然而仅有顺序结构并不能解决所有的问题，比如我们设计一个游戏，游戏第一关的通关条件是玩家获得1000分，那么在完成本局游戏后我们要根据玩家得到分数来决定究竟是进入第二关还是告诉玩家“Game Over”，这里就会产生两个分支，而且这两个分支只有一个会被执行，这就是程序中分支结构。类似的场景还有很多，给大家一分钟的时间，你应该可以想到至少5个以上这样的例子，赶紧试一试。

### if语句的使用

在Python中，要构造分支结构可以使用if、elif和else关键字。所谓关键字就是有特殊含义的单词，像if和else就是专门用于构造分支结构的关键字，很显然你不能够使用它作为变量名（事实上，用作其他的标识符也是不可以）。下面的例子中演示了如何构造一个分支结构。

```python
"""用户身份验证"""

username = input('请输入用户名: ')
password = input('请输入口令: ')
# 如果希望输入口令时 终端中没有回显 可以使用getpass模块的getpass函数
# import getpass
# password = getpass.getpass('请输入口令: ')
if username == 'admin' and password == '123456':
	print('身份验证成功!')
else:
	print('身份验证失败!')
```

唯一需要说明的是和C/C++、Java等语言不同，Python中没有用花括号来构造代码块而是使用了`缩进`的方式来设置代码的层次结构，如果`if`条件成立的情况下需要执行多条语句，只要保持多条语句具有相同的缩进就可以了，换句话说连续的代码如果又保持了相同的缩进那么它们属于同一个代码块，相当于是一个执行的整体。
***
当然如果要构造出更多的分支，可以使用`if…elif…else…`结构，例如下面的分段函数求值。

```python
"""
分段函数求值

        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)

"""

x = float(input('x = '))
if x > 1:
	y = 3 * x - 5
elif x >= -1:
	y = x + 2
else:
	y = 5 * x + 3
print('f(%.2f) = %.2f' % (x, y))
```

当然根据实际开发的需要，分支结构是可以嵌套的，例如判断是否通关以后还要根据你获得的宝物或者道具的数量对你的表现给出等级（比如点亮两颗或三颗星星），那么我们就需要在`if`的内部构造出一个新的分支结构，同理`elif`和`else`中也可以再构造新的分支，我们称之为`嵌套的分支结构`，也就是说上面的代码也可以写成下面的样子。
```python
"""
分段函数求值
		3x - 5	(x > 1)
f(x) =	x + 2	(-1 <= x <= 1)
		5x + 3	(x < -1)

"""

x = float(input('x = '))
if x > 1:
	y = 3 * x - 5
else:
	if x >= -1:
		y = x + 2
	else:
		y = 5 * x + 3
print('f(%.2f) = %.2f' % (x, y))
```
> **`说明`**：大家可以自己感受一下这两种写法到底是哪一种更好。在之前我们提到的Python之禅中有这么一句话`“Flat is better than nested.”`，之所以提出这个观点是因为嵌套结构的嵌套层次多了之后会严重的影响代码的可读性，如果可以使用扁平化的结构就不要去用嵌套，因此之前的写法是更好的做法。

## 练习

### 练习1：英制单位与公制单位互换

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
created on 2019/5/3
@user: Keekuun
功能描述:
    英制单位英寸和公制单位厘米互换
"""

value = float(input('请输入长度：'))
unit = input('请输入单位：')
if (unit in ['in', '英寸']):
    print('%f英寸 = %f厘米' % (value, value * 2.54))
elif (unit in ['cm', '厘米']):
    print('%f厘米 = %f英寸' % (value, value * 2.54))
else:
    print('请输入有效的单位')

```
console结果：
```markdown
请输入长度：10
请输入单位：cm
10.000000厘米 = 25.400000英寸
```

### 练习2：掷骰子决定做什么

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
created on 2019/5/3
@user: Keekuun
功能描述:
    掷骰子决定做什么事情
"""

from random import randint

# get random number 1-6
face = randint(1, 6)
print(face)

if face == 1:
    res = 'lol'
elif face == 2:
    res = 'lol'
elif face == 3:
    res = 'python'
elif face == 4:
    res = 'spider!'
elif face == 5:
    res = 'what you like!'
else:
    res = 'nothing!'

print('play ' + res)

```

console结果：
```markdown
1
play lol
```

### 练习3：百分制成绩转等级制

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
created on 2019/5/3
@user: Keekuun
功能描述：
    百分制成绩转等级制成绩
    90分以上          --> A
    80分~89分         --> B
    70分~79分	      --> C
    60分~69分         --> D
    60分以下          --> E
"""

score = float(input('请输入成绩： '))

if score >= 90:
    rank = 'A'
elif score >= 80:
    rank = 'B'
elif score >= 70:
    rank = 'C'
elif score >= 60:
    rank = 'D'
else:
    rank = 'E'
print('对应的等级是:', rank)
```

console结果：
```markdown
请输入成绩： 88
对应的等级是: B
```

### 练习4：输入三条边长如果能构成三角形就计算周长和面积

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
created on 2019/5/3
@user: Keekuun
功能描述：
    判断输入的边长能否构成三角形
    如果能则计算出三角形的周长和面积
"""

import math

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a + b > c and a + c > b and b + c > a:
    print('周长: %f' % (a + b + c))
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print('面积: %f' % (area))
else:
    print('不能构成三角形')


```
> **`说明`**：上面的代码中使用了math模块的sqrt函数来计算平方根。用边长计算三角形面积的公式叫做[海伦-秦九韶公式](https://zh.wikipedia.org/zh-hans/%E6%B5%B7%E4%BC%A6%E5%85%AC%E5%BC%8F)。

console结果：
```markdown
a = 1
b = 2
c = 3
不能构成三角形
```

### 练习5：个人所得税计算器。

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
created on 2019/5/3
@user: Keekuun
功能描述:
    输入月收入和五险一金计算个人所得税
"""

salary = float(input('本月收入: '))
insurance = float(input('五险一金: '))
diff = salary - insurance - 5000
if diff <= 0:
    rate = 0
    deduction = 0
elif diff < 1500:
    rate = 0.03
    deduction = 0
elif diff < 4500:
    rate = 0.1
    deduction = 105
elif diff < 9000:
    rate = 0.2
    deduction = 555
elif diff < 35000:
    rate = 0.25
    deduction = 1005
elif diff < 55000:
    rate = 0.3
    deduction = 2755
elif diff < 80000:
    rate = 0.35
    deduction = 5505
else:
    rate = 0.45
    deduction = 13505
tax = abs(diff * rate - deduction)
print('个人所得税: ￥%.2f元' % tax)
print('实际到手收入: ￥%.2f元' % (diff + 5000 - tax))

```

console结果：
```markdown
本月收入: 4000
五险一金: 100
个人所得税: ￥0.00元
实际到手收入: ￥3900.00元
```