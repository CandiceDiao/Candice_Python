'''
树  测试类
test_Tree.py
'''

"""
    <html>
        <head>
            <c></c>
            <d></d>
        </head>
        <body>
            <m>
                <n></n>
            </m>
        </body>
    </html>
"""
from DataStructure.Tree.Tree import Tree


class TestTree:

    def test_create_tree(self):
        root = Tree("html")
        head = Tree("head")
        a = Tree("a")
        b = Tree("b")
        # children 为一个list 所以使用append进行扩充
        head.children.append(a)
        head.children.append(b)
        body = Tree("body")
        m = Tree("m")
        x = Tree("x")
        m.children.append(x)
        body.children.append(m)
        root.children.append(head)
        root.children.append(body)

        for node, depth in root.travel():
            print(f"{'  ' * depth}{node} depth={depth}")





