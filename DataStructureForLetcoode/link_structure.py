"""
链表 常用操作
"""
###创建链表
from collections import deque
#使用队列创建链表
linkedlist = deque()

###尾部添加元素
#时间复杂度：O（1）
linkedlist.append(1)
linkedlist.append(2)
linkedlist.append(3)
###中间添加元素
#时间复杂度：O（N）
linkedlist.insert(2,99)
print(linkedlist)

###访问元素
#时间复杂度：O（N）
element = linkedlist[2]
# 99
print(element)

##搜索元素
#时间复杂度：O（N）
index = linkedlist.index(99)
#2
print(index)

##更新元素
#时间复杂度：O（N）
linkedlist[2]=88
#[1,2,88,3]
print(linkedlist)

###删除元素
#时间复杂度：O（N）
#删除指定索引处的值
del linkedlist[2]
#删除某个值
linkedlist.remove(88)

###长度
#时间复杂度：O（1）
length = len(linkedlist)
