"""
yeild
带yield的函数是一个生成器，而不是一个函数了
这个生成器有一个函数就是next函数，next就相当于“下一步”生成哪个数，
这一次的next开始的地方是接着上一次的next停止的地方执行的，
所以调用next的时候，生成器并不会从foo函数的开始执行，只是接着上一步停止的地方开始，
然后遇到yield后，return出要生成的数，此步就结束。
"""

def foo():
    print("starting...")
    while True:
        res = yield 4
        print("res:",res)

def test_foo():
    g = foo()
    print(next(g))
    print("*" * 20)
    print(next(g))

"""
send是发送一个参数给res的
send方法中包含next()方法，所以程序会继续向下运行执行print方法，然后再次进入while循环
"""
def test_send():
    g = foo()
    print(next(g))
    print("*" * 20)
    print(g.send(7))


## 使用yield 实现生成1-10列表
def createlist(num):
    print("starting...")
    while num<10:
        num=num+1
        yield num

def test_create():
    for n in createlist(0):
        print(n)
