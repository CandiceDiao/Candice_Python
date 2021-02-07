"""496 栈
给你两个 没有重复元素 的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。

请你找出 nums1 中每个元素在 nums2 中的下一个比其大的值。

nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出 -1

输入: nums1 = [2,4], nums2 = [1,2,3,4].
输出: [3,-1]
"""
from typing import List


class Solution(object):
    def nextGreaterElement(self,nums1,nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        stack =[]
        # 将num2值放到栈stack中
        for num in nums2:
            stack.append(num)

        for num1 in nums1:
            #temp用来记录从nums2中删除的元素
            #因为找到元素后，还要将删除的元素再加回到栈中
            temp = []
            isFound=False
            max=-1
            while(len(stack)!=0 and not isFound):
                top = stack.pop()
                if top>num1:
                    max = top
                elif top==num1:
                    #找到元素停止遍历
                    isFound=True
                temp.append(top)
            result.append(max)
            #将temp中的元素再一次加入回stack
            while len(temp) !=0:
               stack.append(temp.pop())
        return result

s = Solution()
print(s.nextGreaterElement([2, 4], [1, 2, 3, 4]))
