"""
二叉树类
BTree.py
"""
class BTree:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    #二叉树前序遍历 （使用递归）
    def travel_root(self,subtree):
        item = subtree
        if item is None:
            return
        print(item.data)
        self.travel_root(item.left)
        self.travel_root(item.right)

    #二叉树前序遍历 （使用递归）
    def travel_left(self,subtree):
        item = subtree
        if item is None:
            return
        self.travel_left(item.left)
        print(item.data)
        self.travel_left(item.right)


    #二叉树前序遍历 （使用递归）
    def travel_right(self,subtree):
        item = subtree
        if item is None:
            return
        self.travel_right(item.left)
        self.travel_right(item.right)
        print(item.data)

    #求树深度
    def max_depth(self,subtree,max_depth):
        if subtree is None:
            return max_depth
        #将左子数的结果 赋值给max_left
        max_left = self.max_depth(subtree.left,max_depth+1)
        max_right = self.max_depth(subtree.right,max_depth + 1)
        #比较左右子数深度值，将最大值返回
        return max_left if max_left > max_right else max_right

