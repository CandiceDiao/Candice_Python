"""
树 实现类
Tree.py
"""

class Tree:

    # 树和二叉树的区别：二叉树有 left 和 right，而多叉树只需要一个列表来表达就可以了
    def __init__(self,data):
        self.data = data
        self.children = []

    #遍历树
    def travel(self, node=None,depth=1):
        if node is None:
             node = self
        yield (node.data,depth)
        depth += 1
        for child in node.children:
            yield from self.travel(child)
        depth -= 1

    # 根据XML创建树
    def create_from_string(self,content)->'Tree':
        pass

