"""
测试二叉树
test_BTree.py
"""
from DataStructure.BTree.BTree import BTree


class TestBTree:

    # demo 二叉树数据
    """
    0
    1 2
    3 4 | 5 6
    none none |none none |none none|7 none|
    """
    def setup(self):
        self.tree = BTree(0)
        self.tree.left = BTree(1)
        self.tree.left.left = BTree(3)
        self.tree.left.right = BTree(4)
        self.tree.right = BTree(2)
        self.tree.right.left = BTree(5)
        self.tree.right.right = BTree(6)
        self.tree.right.right.left = BTree(7)

    def test_travel(self):
        # self.tree.travel_root(self.tree) #===》0 1 3 4 2 5 6 7
        # self.tree.travel_left(self.tree)   #===> 3 1 4 0 5 2 6 7
        self.tree.travel_right(self.tree)   #===> 3 4 1 5 7 6 2 0

    def test_max_depth(self):
        assert 4 == self.tree.max_depth(self.tree, 0)
        #再次添加数子节点
        self.tree.right.right.left.left= BTree(8)
        assert 5 == self.tree.max_depth(self.tree, 0)

