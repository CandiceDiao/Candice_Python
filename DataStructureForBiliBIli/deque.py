'''
双端队列： 队头和队尾相当于栈
'''

"""
操作
Deque() 创建一个空的双端队列
add_front(item) 从队头加入一个item元素
add_rear(item) 从队尾加入一个item元素
remove_front() 从队头删除一个item元素
remove_rear() 从队尾删除一个item元素
is_empty() 判断双端队列是否为空
size() 返回队列的大小
"""
class Deque():

    def __init__(self):
        # 用顺序表实现队列
        self.__list = []

    # add_front(item) 从队头加入一个item元素
    def add_fron(self, item):
        self.__list.insert(0,item)

    #add_rear(item) 从队尾加入一个item元素
    def add_rear(self, item):
        self.__list.append(item)

    #remove_front() 从队头删除一个item元素
    def remove_front(self):
        return self.__list.pop(0)

    #remove_rear() 从队尾删除一个item元素
    def remove_rear(self):
        return self.__list.pop()

    # is_empty() 判断一个队列是否为空
    def is_empty(self):
        return not self.__list

    # size() 返回队列的大小
    def size(self):
        return len(self.__list)

if __name__=='__main__':
    s = Deque()
    s.add_fron(1)
    s.add_fron(2)
    s.add_rear(3)
    s.add_rear(4)
    print(s.remove_front())
    print(s.remove_front())
    print(s.remove_rear())
    print(s.remove_rear())



