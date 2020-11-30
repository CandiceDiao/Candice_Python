"""
链表实现类
link.py
"""
class Link:

    def __init__(self,data):
        #链表数据部分
        self.data = data
        #链表指针部分
        #next 永远指向下一个节点，在初始化时链表是空的所以让它先等于 None。
        self.next = None

    # 追加列表
    def append(self,data=None):
        item = self
        while item.next is not None:
            # 使用 item 等于 item.next，直到下一个节点为空就可以得到链表的尾部节点
            item = item.next
        #使用 item.next 等于 LinkNode 就可以在尾部追加一个数据
        item.next = Link(data)
        return self

    #遍历列表
    def travel(self):
        item = self
        # while 循环条件为什么不能是item.next is not None
        # 这样的话会漏掉最后一个节点
        while item is not None:
            print(item.data)
            item = item.next

    #查找位置
    def search(self,data):
        index =0
        item = self
        while item is not None:
            if item.data == data:
                return index
            else:
                index += 1
                item=item.next
        return -1

    #插入数据
    def insert(self,pop,data):
        index = 0

        item = self
        while item is not None:
            if index == (pop-1):
                break
            index +=1
            item = item.next
        node = Link(data)
        # 注意顺序 要先将node->item.next
        node.next = item.next
        item.next = node

    # 链表生成器：获取链表中的每一个元素
    def get_item(self):
        item = self
        while item is not None:
            #获取链表中的每一个元素
            yield item
            item = item.next

    # 排序
    def order(self,data):
        pre = self
        #使用 for item in self.get_item() 把链表的每个元素全都调用一遍，
        # 通过这个方法可以获得每一个节点。
        for item in self.get_item():
            if data < item.data:
                break
            #因为是单向列表
            # pre 变量，保存之前遍历过的元素
            pre = item
        # 同列表插入
        node_new = Link(data)
        node_new.next = pre.next
        pre.next = node_new
        return self



