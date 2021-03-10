"""21  合并两个有序链表
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]
"""

#时间复杂度O(N)
class Solution(object):
    def mergeTwoLists(self, l1:ListNode, l2:ListNode)->ListNode:
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode()
        cur = res
        while(l1 !=None and l2 !=None):
            if l1.val <= l2.val:
                cur.next = l1
                #指向l1的下一个节点
                l1=l1.next
            else:
                cur.next = l2
                l2=l2.next
            cur=cur.next
        # 当一个链表走完后为空，直接将另一个链表剩下部分拼接上即可
        cur.next=l1 or l2
        return res.next