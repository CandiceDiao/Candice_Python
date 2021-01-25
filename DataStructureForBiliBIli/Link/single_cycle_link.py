"""
单向循环链表
"""
#节点
class Node(object):
    def __init__(self,elem):
        #保存数据
        self.elem = elem
        #保存下一个节点地址
        self.next = None

#单向循环链表
"""
单链表的操作
is_empty() 链表是否为空
length() 链表长度
travel() 遍历整个链表
add(item) 链表头部添加元素
append(item) 链表尾部添加元素
insert(pos, item) 指定位置添加元素
remove(item) 删除节点
search(item) 查找节点是否存在"""
class SingleCycleLinkList(object):

    def __init__(self,node=None):
        self.__head = node
        #当构造一个不是空的链表，需要指向它自己
        if node:
            node.next = node

    #链表是否为空
    def is_empty(self):
        # 与None比较最好使用is 不是==
        return self.__head is None

    #链表长度
    def length(self):
        # 空链表的特殊情况
        if self.is_empty():
            return 0
        cur = self.__head
        #由于循环终止条件，指到链表最后一个节点，所以count值应为1
        count = 1
        #不可以使用while cur ==self.__head:作为判断条件
        #因为第一次的时候一进来 cur 就等于self.__head
        while cur.next != self.__head:
            count += 1
            cur = cur.next
        return count

    #遍历整个链表
    def travel(self):
        #空链表
        if self.is_empty():
            return
        cur =self.__head
        while cur.next != self.__head:
            print(cur.elem,end=" ")
            cur = cur.next
        # 退出循环时，cur指向尾节点，但尾节点的元素未打印
        print(cur.elem)


    #链表头部添加元素 头插法
    def add(self,item):
        node = Node(item)
        #空链表特殊情况
        if self.is_empty():
            self.__head=node
            node.next=node
        else:
            # 先找到尾节点
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            # 循环退出时 cur为尾节点
            node.next = self.__head
            self.__head = node
            # 最后游标指向两种写法
            # cur.next = node
            cur.next = self.__head


    #链表尾部添加元素 尾插法
    def append(self,item):
        node = Node(item)
        cur = self.__head
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            while cur.next != self.__head:
                cur = cur.next
            node.next = self.__head
            #node.next = current.next
            cur.next = node

    #指定位置添加元素 同单链表
    def insert(self,pos,item):
        if pos<=0:
            self.add(item)
        elif pos>(self.length()-1):
            self.append(item)
        else:
            # 指向第一个节点
            pre = self.__head
            count = 0
            while count < (pos - 1):
                pre = pre.next
                count += 1
            node = Node(item)
            # 循环退出后，pre指向pos-1位置
            node.next = pre.next
            pre.next = node


    #删除节点
    '''
    *删除头节点
    只有头节点
    删除为尾节点
    '''
    def remove(self,item):
        cur = self.__head
        pre = None
        if self.is_empty():
            return
        while cur.next != self.__head:
            if cur.elem == item:
                #头节点
                if cur ==self.__head:
                    #找到尾节点
                    rear = self.__head
                    while rear.next !=self.__head:
                        rear = rear.next
                    self.__head = cur.next
                    rear.next = self.__head
                else:
                    #中间节点删除操作同单链表
                    pre.next = cur.next
                #break
                # 单向循环列表时，不能用break，因为退出循环之后还要在判断最后一个元素
                return
            else:
                pre = cur
                cur = cur.next
        #跳出循环 cur指向尾节点
        if cur.elem==item:
            #链表只有一个节点特殊情况
            if cur == self.__head:
                self.__head = None
            else:
                pre.next = cur.next
                #pre.next = self.__head


    #查找节点是否存在
    def search(self,item):
        cur = self.__head
        #空链表特殊情况
        if self.is_empty():
            return False
        while cur.next != self.__head :
            if cur.elem == item:
                return True
            else:
                cur =cur.next
        # 退出循环时，cur指向尾节点，所以需要判断一下尾节点元素
        if cur.elem == item:
            return True
        return False

if __name__=='__main__':
    ll = SingleCycleLinkList()
    print(ll.is_empty())
    print(ll.length())

    ll.append(1)
    print(ll.is_empty())
    print(ll.length())

    ll.append(2)
    ll.add(8)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    # 8123456
    ll.insert(-1,9) # 98123456
    ll.travel()
    ll.insert(3,100) #9 8 100 1 2 3 4 5 6
    ll.travel()
    ll.insert(10,200) #9 8 100 1 2 3 4 5 6 200
    ll.travel()
    ll.remove(100)
    ll.travel()
    ll.remove(9)
    ll.travel()
    ll.remove(200)
    ll.travel()


