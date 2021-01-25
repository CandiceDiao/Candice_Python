"""
双向链表
"""
#节点


class Node(object):
    def __init__(self,item):
        self.elem = item
        self.next = None
        #前驱节点
        self.prev = None

#双链表
    # class DoubleLinkList(SingleLinkList):
    # 继承单链表类class DoubleLinkList(SingleLinkList):
    # 与单链表相同部分，均可使用单链表的方法
    #但是单链表中__head不可定义为私有变量！！！

class DoubleLinkList(object):
    def __init__(self,node=None):
        #双链表头节点（p）：把第一个节点挂到链表上
        #与单链表一致
        self.__head = node

    #链表是否为空 与单链表相同
    def is_empty(self):
        return self.__head is None

    #链表长度 与单链表相同
    def length(self):
        # cur游标，用来移动，遍历节点
        cur = self.__head
        #count 记录数量
        count = 0
        while cur != None:
            count +=1
            cur = cur.next
        return count

    #遍历整个链表 与单链表相同
    def travel(self):
        cur =self.__head
        while cur !=None:
            print(cur.elem,end=" ")
            cur = cur.next
        print(" ")

    #查找节点是否存在 与单链表相同
    def search(self,item):
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur =cur.next
        return False


    #链表头部添加元素 头插法
    def add(self,item):
        node = Node(item)
        node.next = self.__head
        self.__head.pre = node
        self.__head = node


    #链表尾部添加元素 尾插法
    def append(self,item):
        node = Node(item)
        cur = self.__head
        if self.is_empty():
            self.__head = node
        else:
            while cur.next != None:
                cur = cur.next
            cur.next = node
            node.prev = cur

    #指定位置添加元素
    def insert(self,pos,item):
        if pos<=0:
            self.add(item)
        elif pos>(self.length()-1):
            self.append(item)
        else:
            # 指向第一个节点
            cur = self.__head
            count = 0
            while count < pos:
                count += 1
                cur = cur.next
            node = Node(item)
            node.next = cur
            node.prev = cur.prev
            #方式一：先将前面的节点指向新节点；在将后面的节点指向新节点
            cur.prev.next = node
            cur.prev = node
            # #方式二：先将后面的节点指向新节点；再将前面的节点指向新节点
            # cur.prev = node
            # node.prev.next = node


    #删除节点
    '''
    *删除头节点
    只有头节点
    删除为尾节点
    '''
    def remove(self,item):
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                #先判断此节点是否为头节点
                #如果是头节点：prev==None 或者 cur = self.__head
                if cur ==self.__head:
                    self.__head = cur.next
                    #判断链表是否只有一个节点的特殊情况
                    if cur.next:
                       cur.next.prev = None
                else:
                    cur.prev.next = cur.next
                    # 判断删除元素为链表最后一个元素特殊情况
                    if cur.next:
                       cur.next.prev = cur.prev
                break
            else:
                cur = cur.next


if __name__=='__main__':
    dll = DoubleLinkList()

    print(dll.is_empty())
    print(dll.length())

    dll.append(1)
    print(dll.is_empty())
    print(dll.length())

    dll.append(2)
    dll.add(8)
    dll.append(3)
    dll.append(4)
    dll.append(5)
    dll.append(6)
    # 8123456
    dll.insert(-1, 9)  # 98123456
    dll.travel()
    dll.insert(3, 100)  # 9 8 100 1 2 3 4 5 6
    dll.travel()
    dll.insert(10, 200)  # 9 8 100 1 2 3 4 5 6 200
    dll.travel()
    dll.remove(100)
    dll.travel()
    dll.remove(9)
    dll.travel()
    dll.remove(200)
    dll.travel()