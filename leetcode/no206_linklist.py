"""206 链表
反转一个单链表。

示例:
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
"""

class Solution(object):
    def reverseList(self, head:ListNode)->ListNode:
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        while head is not None and head.next is not None:
            denxt = dummy.next
            hnext = head.next

            #dummy-2
            dummy.next=hnext
            #1-3
            head.next = hnext.next
            #2-1
            hnext.next=denxt
        return dummy.next



