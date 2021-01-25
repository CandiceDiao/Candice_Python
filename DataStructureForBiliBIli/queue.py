'''
队列 LIFO
用顺序表实现队列
'''

"""
操作
Queue() 创建一个空的队列
enqueue(item) 往队列中添加一个item元素
dequeue() 从队列头部删除一个元素
is_empty() 判断一个队列是否为空
size() 返回队列的大小
"""
class Queue():
    def __init__(self):
        #用顺序表实现队列
        self.__list = []

    #enqueue(item) 往队列中添加一个item元素
    def enqueue(self,item):
        #*在尾部添加，头部出；还是从头部添加尾部出 需要对比队列的入队，出队操作那个比较多
        #末尾追加
        self.__list.append(item)

    #dequeue() 从队列头部删除一个元素
    def dequeue(self):
        # 从尾部添加元素，就必须头部弹出
        return self.__list.pop(0)

    #is_empty() 判断一个队列是否为空
    def is_empty(self):
        return not self.__list

    #size() 返回队列的大小
    def size(self):
        return len(self.__list)

if __name__=='__main__':
    s = Queue()
    s.enqueue(1)
    s.enqueue(2)
    s.enqueue(3)
    s.enqueue(4)
    print(s.dequeue())
    print(s.dequeue())
    print(s.dequeue())
    print(s.dequeue())


