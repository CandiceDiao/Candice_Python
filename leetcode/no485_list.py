""" 485 数组
给定一个二进制数组， 计算其中最大连续1的个数。

示例 1:

输入: [1,1,0,1,1,1]
输出: 3
解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.
注意：

输入的数组只包含 0 和1。
输入数组的长度是正整数，且不超过 10,000
"""

# class Solution(object):
#     def findMaxConsecutiveOnes(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         count=0
#         for i in range(len(nums)-1):
#             for j in range(1,len(nums)):
#                 if nums[i]==nums[j]:
#                     count+=1
#                 else:
#                     count=0
#         return count
#
# s=Solution()
# print(s.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
"""
存在问题：每次连续结束后得到的count与上一个连续的count比较 而不是仅返回最后一个连续的count
"""
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        if nums is None or len(nums)==0:
            return 0
        count = 0
        result =0
        for i in range(len(nums)):
            if nums[i] == 1:
                count+=1
            else:
                result = max(result,count)
                count =0
        return max(result,count)

s=Solution()
print(s.findMaxConsecutiveOnes([1,1,1,0,0,0,0,1,1]))


