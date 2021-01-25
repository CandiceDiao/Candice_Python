'''
栈 LIFO
用顺序表实现栈
'''


'''
栈的操作
Stack() 创建一个新的空栈
push(item) 添加一个新的元素item到栈顶
pop() 弹出栈顶元素
peek() 返回栈顶元素
is_empty() 判断栈是否为空
size() 返回栈的元素个数
'''
class Stack(object):

    def __init__(self):
        #用顺序表实现栈
        self.__list = []

    #push(item) 添加一个新的元素item到栈顶
    def push(self,item):
        # 从链表的尾部去压
        #使用顺序表实现栈，应该从尾部去添加和弹出：因为顺序表尾部操作时间复杂度为O(1),而头部时间复杂度为O（n）
        self.__list.append(item)
        # # 定义从头部添加
        # self.__list.insert(0,item)

    #pop() 弹出栈顶元素
    def pop(self):
        # 从链表的尾部去取
        return self.__list.pop()
        # # 如果push定义的从头部添加，那么pop就必须从头部弹出
        # self.__list.pop(0)

    #peek() 返回栈顶元素
    def peek(self):
        if self.__list:
            return self.__list[-1]
        else:
            #空列表的特殊情况
            return None

    #is_empty() 判断栈是否为空
    def is_empty(self):
        # return self.__list == []
        # 空字符串""，0，空字典{}，空列表[]---》均为False
        return not self.__list

    #size() 返回栈的元素个数
    def size(self):
        return len(self.__list)

if __name__=='__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())





