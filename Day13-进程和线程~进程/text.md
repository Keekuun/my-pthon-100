# 进程和线程

今天我们使用的计算机早已进入多CPU或多核时代，而我们使用的操作系统都是支持“多任务”的操作系统，这使得我们可以同时运行多个程序，也可以将一个程序分解为若干个相对独立的子任务，让多个子任务并发的执行，从而缩短程序的执行时间，同时也让用户获得更好的体验。因此在当下不管是用什么编程语言进行开发，实现让程序同时执行多个任务也就是常说的“并发编程”，应该是程序员必备技能之一。为此，我们需要先讨论两个概念，一个叫**进程**，一个叫**线程**。

## 概念

进程就是操作系统中执行的一个程序，操作系统以进程为单位分配存储空间，每个进程都有自己的地址空间、数据栈以及其他用于跟踪进程执行的辅助数据，操作系统管理所有进程的执行，为它们合理的分配资源。进程可以通过`fork`或`spawn`的方式来创建新的进程来执行其他的任务，不过新的进程也有自己独立的内存空间，因此必须通过`进程间通信机制`（IPC，Inter-Process Communication）来实现数据共享，具体的方式包括`管道`、`信号`、`套接字`、`共享内存区`等。

一个进程还可以拥有多个并发的执行线索，简单的说就是拥有多个可以获得CPU调度的执行单元，这就是所谓的线程。由于线程在同一个进程下，它们可以共享相同的上下文，因此相对于进程而言，线程间的信息共享和通信更加容易。当然在单核CPU系统中，真正的并发是不可能的，因为在某个时刻能够获得CPU的只有唯一的一个线程，多个线程共享了CPU的执行时间。使用多线程实现并发编程为程序带来的好处是不言而喻的，最主要的体现在提升程序的性能和改善用户体验，今天我们使用的软件几乎都用到了多线程技术，这一点可以利用系统自带的进程监控工具（如macOS中的“活动监视器”、Windows中的“任务管理器”）来证实，如下图所示(win10任务管理器)。
![进程](./img/process.png)

## 理解进程和线程

- `对于操作系统来说，一个任务就是一个进程（Process）`，比如打开一个浏览器就是启动一个浏览器进程，打开一个记事本就启动了一个记事本进程，打开两个记事本就启动了两个记事本进程，打开一个Word就启动了一个Word进程。
- 有些进程还不止同时干一件事，比如Word，它可以同时进行打字、拼写检查、打印等事情。在一个进程内部，要同时干多件事，就需要同时运行多个“子任务”，我们把`进程内的这些“子任务”称为线程（Thread）`。由于每个进程至少要干一件事，所以，`一个进程至少有一个线程`。
- 多任务的实现有3种方式：
    - 多进程模式；
    - 多线程模式；
    - 多进程+多线程模式。
    

线程是最小的执行单元，而进程由至少一个线程组成。如何调度进程和线程，完全由操作系统决定，程序自己不能决定什么时候执行，执行多长时间。
多进程和多线程的程序涉及到同步、数据共享的问题，编写起来更复杂。

下面用一个下载文件的例子来说明使用多进程和不使用多进程到底有什么差别，先看看下面的代码。

不使用进程：
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
created on 2019/5/11
@user: Keekuun
功能描述：
    模拟普通下载文件
"""

from random import randint
from time import time, sleep


def download_task(filename):
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))


def main():
    start = time()
    download_task('Python从入门到精通.pdf')
    download_task('Peking Hot.avi')
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))


if __name__ == '__main__':
    main()
```
console结果：
```shell
开始下载Python从入门到精通.pdf...
Python从入门到精通.pdf下载完成! 耗费了5秒
开始下载Peking Hot.avi...
Peking Hot.avi下载完成! 耗费了6秒
总共耗费了11.00秒.

Process finished with exit code 0
```
从上面的例子可以看出，如果程序中的代码只能按顺序一点点的往下执行，那么即使执行两个毫不相关的下载任务，也需要`先等待一个文件下载完成后才能开始下一个下载任务`，很显然这并不合理也没有效率。

下面我们通过多进程的方式实现。首先我们先来学习Python中的多进程。


## Python中的多进程

要让Python程序实现多进程（multiprocessing），我们先了解操作系统的相关知识。

Unix/Linux操作系统提供了一个`fork()`系统调用，它非常特殊。普通的函数调用，调用一次，返回一次，但是fork()调用一次，返回两次，因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回。

子进程永远返回0，而父进程返回子进程的ID。这样做的理由是，`一个父进程可以fork出很多子进程`，所以，父进程要记下每个子进程的ID，而子进程只需要调用`getppid()`就可以拿到父进程的ID。

Python的os模块封装了常见的系统调用，其中就包括fork，可以在Python程序中轻松创建子进程：

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
created on 2019/5/11
@user: Keekuun
功能描述：
     Unix/Linux/Mac系统下fork调用创建子进程
"""

import os

print('Process (%s) start...' % os.getpid())
# Only works on Unix/Linux/Mac:
pid = os.fork()
if pid == 0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

```

由于Windows没有fork调用，上面的代码在Windows上无法运行。
```shell
AttributeError: module 'os' has no attribute 'fork'
```

有了fork调用，一个进程在接到新任务时就可以复制出一个子进程来处理新任务，常见的Apache服务器就是由父进程监听端口，每当有新的http请求时，就fork出子进程来处理新的http请求。

### multiprocessing模块
如果你打算编写多进程的服务程序，Unix/Linux无疑是正确的选择。由于Windows没有fork调用，难道在Windows上无法用Python编写多进程的程序？
由于Python是跨平台的，自然也应该提供一个跨平台的多进程支持。multiprocessing模块就是跨平台版本的多进程模块。
`multiprocessing`模块提供了一个`Process`类来代表一个进程对象。下面我们用Process来开启多进程模拟前面的下载任务。

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
created on 2019/5/11
@user: Keekuun
功能描述
    开启多进程模拟下载文件
"""

from multiprocessing import Process
from os import getpid
from random import randint
from time import time, sleep


def download_task(filename):
    print('启动下载进程，进程号[%d].' % getpid())
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))


def main():
    start = time()
    # 开启进程1
    p1 = Process(target=download_task, args=('Python从入门到精通.pdf',))
    p1.start()
    # 开启进程2
    p2 = Process(target=download_task, args=('Peking Hot.avi',))
    p2.start()
    # 进程间的同步
    p1.join()
    p2.join()
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))


if __name__ == '__main__':
    main()

```

在上面的代码中，我们通过`Process类`创建了进程对象，通过`target参数`我们传入一个函数来表示进程启动后要执行的代码，后面的`args`是一个`元组`，它代表了传递给函数的`参数`。Process对象的`start`方法用来启动进程，而`join`方法表示等待进程执行结束。运行上面的代码可以明显发现两个下载任务“同时”启动了，而且程序的执行时间将大大缩短，不再是两个任务的时间总和。下面是程序的一次执行结果。

console结果
```shell
启动下载进程，进程号[21860].
开始下载Python从入门到精通.pdf...
启动下载进程，进程号[43300].
开始下载Peking Hot.avi...
Python从入门到精通.pdf下载完成! 耗费了6秒
Peking Hot.avi下载完成! 耗费了8秒
总共耗费了8.31秒.

Process finished with exit code 0

```

创建子进程时，只需要传入一个执行函数`target`和函数的参数`args`，创建一个`Process实例`，用`start()`方法启动，这样创建进程比`fork()`还要简单。
`join()`方法可以等待子进程结束后再继续往下运行，通常用于`进程间的同步`

### 子进程
很多时候，子进程并不是自身，而是一个外部进程。我们创建了子进程后，还需要控制子进程的输入和输出。
`subprocess模块`可以让我们非常方便地启动一个子进程，然后控制其输入和输出。
````python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
created on 2019/5/11
@user: Keekuun
功能描述:
    子进程
"""

import subprocess

print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('gbk'))
print('Exit code:', p.returncode)

````
上面的代码相当于在命令行执行命令`nslookup`，然后手动输入：
```
set q=mx
python.org
exit
```

console结果：
```shell
$ nslookup
默认服务器:  UnKnown
Address:  192.168.42.129

> > 服务器:  UnKnown
Address:  192.168.42.129

python.org	MX preference = 50, mail exchanger = mail.python.org
> 
Exit code: 0
```
>参考文档：[subprocess](https://docs.python.org/3.6/library/subprocess.html)
### Pool
如果要启动大量的子进程，可以用进程池的方式批量创建子进程：
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
created on 2019/5/11
@user: Keekuun
功能描述
    启动大量进程---进程池Pool
"""

from multiprocessing import Pool
import os, time, random


def long_time_task(name):
    print('Run task %s(%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 5)
    end = time.time()
    print('Task %s runs %.2f seconds.' % (name, (end - start)))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(6):
        # p.apply(long_time_task, args=(i,))
        p.apply_async(long_time_task, args=(i,))  # 异步
    print('Waiting for all subprocess done...')
    p.close()
    p.join()
    print('All subprocess done.')

```
console结果：
```shell
Parent process 78424.
Waiting for all subprocess done...
Run task 0(46796)...
Run task 1(41220)...
Run task 2(58612)...
Run task 3(109256)...
Task 3 runs 2.74 seconds.
Run task 4(109256)...
Task 0 runs 3.74 seconds.
Run task 5(46796)...
Task 1 runs 4.56 seconds.
Task 2 runs 4.89 seconds.
Task 4 runs 3.83 seconds.
Task 5 runs 3.40 seconds.
All subprocess done.

Process finished with exit code 0
```
对`Pool`对象调用`join()`方法会等待所有子进程执行完毕，调用join()之前必须先调用`close()`，调用close()之后就不能继续添加新的Process了。

请注意输出的结果，`task 0，1，2，3`是立刻执行的，而`task 4,5`要等待前面某个task完成后才执行，这是因为Pool开启了4个进程，最多同时执行4个进程。如果改成：`p = Pool(5)`就可以同时跑5个进程。

### 进程间通信
Process之间肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信。Python的multiprocessing模块包装了底层的机制，提供了`Queue`、`Pipes`等多种方式来交换数据。

我们以Queue为例，在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据：

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
created on 2019/5/11
@user: Keekuun
功能描述
    进程间通信
"""

from multiprocessing import Process, Queue
import os, time, random


# 写数据进程执行的任务
def line(q):
    print('欢迎来到召唤师峡谷（战场编号: %s）' % os.getpid())

    for hero in ['蛮', '易', '信']:
        print('%s 上线了' % hero)
        q.put(hero)
        time.sleep(random.random())


# 读数据进程执行的任务
def gank(q):
    print('Gank即将开始（Gank编号: %s）' % os.getpid())
    while True:
        hero = q.get(True)
        print('%s 来Gank了!.' % hero)


if __name__ == '__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pl = Process(target=line, args=(q,))
    pg = Process(target=gank, args=(q,))

    # 启动子进程line
    pl.start()

    # 启动子进程gank
    pg.start()

    # 等待line结束
    pl.join()

    # gank进程里是死循环，无法等待其结束，只能强行终止:
    pg.terminate()

```
console结果：
```shell
欢迎来到召唤师峡谷（战场编号: 75900）
蛮 上线了
Gank即将开始（Gank编号: 59772）
蛮 来Gank了!.
易 上线了
易 来Gank了!.
信 上线了
信 来Gank了!.
```

在Unix/Linux下，multiprocessing模块封装了fork()调用，使我们不需要关注fork()的细节。由于Windows没有fork调用，因此，multiprocessing需要“模拟”出fork的效果，父进程所有Python对象都必须通过pickle序列化再传到子进程去，所有，如果multiprocessing在Windows下调用失败了，要先考虑是不是pickle失败了。

总结
- 在Unix/Linux下，可以使用fork()调用实现多进程。
- 要实现跨平台的多进程，可以使用multiprocessing模块。
- 进程间通信是通过Queue、Pipes等实现的。