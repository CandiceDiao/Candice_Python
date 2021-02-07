"""203 链表
删除链表中等于给定值 val 的所有节点。

示例:

输入: 1->2->6->3->4->5->6, val = 6
输出: 1->2->3->4->5
"""
import queue



class Solution(object):
    def removeElements(self, head: ListNode, val:int):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        prev=dummy
        while head is not None:
            #移除元素
            if head.val ==val:
                prev.next = head.next
            else:
                prev = prev.next
            head = head.next
        return dummy.next


"""
思路
head 指向当前节点
1.需要一个dummy临时节点 指向链表头 dummy.next=head
2.需要一个prev指针，指向之前的节点，这样删除以后才能连接到下一个节点 prev.next=head.next
"""

