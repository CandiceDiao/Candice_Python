"""
测试链表类
test_link.py
"""
from DataStructure.Link.link import Link


class TestLink:

    def setup(self):
        self.link = Link(0)
        self.link.append(11).append(22).append(33)

    def test_link_node_add(self):
        self.link = Link(0)
        self.link.next =Link(1)
        self.link.next.next = Link(2)
        self.link.travel()

    def test_link_node_append(self):
        self.link.append(11).append(22).append(33)
        self.link.travel()

    def test_search(self):
        print(self.link.search(11))
        print(self.link.search(33))

    def test_index(self):
        self.link.insert(1,"new")
        print(self.link.search("new"))


