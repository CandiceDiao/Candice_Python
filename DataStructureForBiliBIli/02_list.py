#测算
import timeit
from timeit import Timer

li1 = []

li1 = [1,2]
li2 = [23,5]

li = li1 +li2

li = [i for i in range(10000)]

li = list(range(10000))

def test1():
    li = []
    for i in range(10000):
        li.append(i)
def test2():
    li = []
    for i in range(10000):
        li += [i]

def test3():
    li = [i for i in range(10000)]

def test4():
    li = list(range(10000))

def test5():
    li = []
    for i in range(10000):
        li.extend([i])

timer1 = Timer("test1()","from __main__ import test1")
#测算1000次;返回执行时间，单位为秒
print('append',timer1.timeit(1000))

timer2 = Timer("test2()","from __main__ import test2")
#测算1000次;返回执行时间，单位为秒
print("+",timer2.timeit(1000))

timer3 = Timer("test3()","from __main__ import test3")
#测算1000次;返回执行时间，单位为秒
print("[i for i in range(1000)]",timer3.timeit(1000))

timer4 = Timer("test4()","from __main__ import test4")
#测算1000次;返回执行时间，单位为秒
print('list',timer4.timeit(1000))

timer5 = Timer("test5()","from __main__ import test5")
#测算1000次;返回执行时间，单位为秒
print('extend',timer5.timeit(1000))
