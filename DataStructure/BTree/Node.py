'''
二叉树节点类
'''

class Node():
    def __init__(self,item):
        self.elem = item
        self.lchild = None
        self.rchild = None

'''
二叉树类
'''
class ByteTree(object):
    def __init__(self):
        # 根节点
        self.root = None

    """
    二叉树增加节点思路：
    将数根节点放入【队列】
    弹出【队首元素】，判断是否存在左右节点
    如果存在则将该元素【放入队列】为了对该节点进行遍历
    如果没有左右节点，增将该元素插入此位置  
    """
    def add(self,item):
        # 将拿到的元素构造成一个节点
        node = Node(item)
        # 如果树是空的，则对根节点赋值
        if self.root == None:
            self.root = node
            return
        # 将根节点放入队列
        queue = [self.root]
        while queue:
            # 从队头取数据
            cur_node = queue.pop(0)
            if cur_node.lchild is None:
                cur_node.lchild = node
                return
            else:
                # 左节点存在，要把左节点放入队列中
                queue.append(cur_node.lchild)
            if cur_node.rchild is None:
                cur_node.rchild = node
                return
            else:
                # 左节点存在，要把左节点放入队列中
                queue.append(cur_node.rchild)


    # 广度遍历：逐层遍历
    def breadth_travel(self):
        # 当根节点为空时
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            #从队列中取出第一个元素
            cur_node = queue.pop(0)
            #打印当前元素
            print(cur_node.elem,end = " ")
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)

    # 深度遍历-先序遍历
    # def preorder(self,node): 中node 为根节点
    def preorder(self,node):
        if node is None:
            return
        print(node.elem, end=" ")
        # node.lchild 传入左子树
        self.preorder(node.lchild)
        # 传入右子树
        self.preorder(node.rchild)

    #中序遍历
    def inorder(self,node):
        if node is None:
            return

        # node.lchild 传入左子树
        self.inorder(node.lchild)
        print(node.elem, end=" ")
        # 传入右子树
        self.inorder(node.rchild)

    #后序遍历
    def postorder(self,node):
        if node is None:
            return
        # node.lchild 传入左子树
        self.postorder(node.lchild)
        # 传入右子树
        self.postorder(node.rchild)
        print(node.elem, end=" ")


if __name__ =='__main__':
    tree = ByteTree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    print("广度遍历")
    tree.breadth_travel()
    print('\n'+"先序遍历")
    tree.preorder(tree.root)
    print('\n'+"中序遍历")
    tree.inorder(tree.root)
    print('\n'+"后序遍历")
    tree.postorder(tree.root)









