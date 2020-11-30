class Node(object):
    """节点类"""
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild

    def add(self, elem):
        """为树添加节点"""
        node = Node(elem)
        #如果树是空的，则对根节点赋值
        if self.root == None:
            self.root = node
        else:
            queue = []
            queue.append(self.root)
            #对已有的节点进行层次遍历
            while queue:
                #弹出队列的第一个元素
                cur = queue.pop(0)
                if cur.lchild == None:
                    cur.lchild = node
                    return
                elif cur.rchild == None:
                    cur.rchild = node
                    return
                else:
                    #如果左右子树都不为空，加入队列继续判断
                    queue.append(cur.lchild)
                    queue.append(cur.rchild)

        # 广度遍历：逐层遍历
        def breadth_travel(self):
            # 当根节点为空时
            if self.root is None:
                return
            queue = [self.root]
            while queue:
                # 从队列中取出第一个元素
                cur_node = queue.pop(0)
                # 打印当前元素
                print(cur_node.elem)
                if cur_node.lchild is not None:
                    queue.append(cur_node.lchild)
                if cur_node.rchild is not None:
                    queue.append(cur_node.rchild)

    if __name__ == '__main__':
        tree = ByteTree()
        tree.add(1)
        tree.add(2)
        tree.add(3)
        tree.add(4)
        tree.add(5)
        tree.breadth_travel()