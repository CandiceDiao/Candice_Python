"""
链表相关面试题
"""


from DataStructure.Link.link import Link


class TestLinkEX:

    ### 创建一个有序的链表，并做有序的数据插入
    def test_order(self):
        self.link = Link(1)
        self.link.order(5).order(3).order(2).order(4)
        link_data = [item.data for item in self.link.get_item()]
        assert link_data == [1,2,3,4,5]


