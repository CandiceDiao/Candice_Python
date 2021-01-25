"""
单链表
"""
#节点
class Node(object):
    def __init__(self,elem):
        #保存数据
        self.elem = elem
        #保存下一个节点地址
        self.next = None

#单链表类
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
class SingleLinkList(object):

    def __init__(self,node=None):
        #单链表头节点（p）：把第一个节点挂到链表上
        #具体的对象使用该属性，所以定义为对象的私有属性
        self.__head = node
        return self.__head

    #链表是否为空
    def is_empty(self):
        # 与None比较最好使用is 不是==
        return self.__head is None

    #链表长度
    def length(self):
        # cur游标，用来移动，遍历节点
        cur = self.__head
        #count 记录数量
        count = 0
        while cur != None:
            count +=1
            cur = cur.next
        return count

    #遍历整个链表
    def travel(self):
        cur =self.__head
        while cur !=None:
            print(cur.elem,end=" ")
            cur = cur.next
        print(" ")

    #链表头部添加元素 头插法
    def add(self,item):
        node = Node(item)
        node.next = self.__head
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

    #指定位置添加元素
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
        while cur != None:
            if cur.elem == item:
                #先判断此节点是否为头节点
                #如果是头节点：pre==None 或者 cur = self.__head
                if cur ==self.__head:
                    #只有头节点情况也可以满足
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    #查找节点是否存在
    def search(self,item):
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur =cur.next
        return False

if __name__=='__main__':
    ll = SingleLinkList()
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


