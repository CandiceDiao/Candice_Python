"""39 数组中出现次数超过一半的数字
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
 
你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例 1:
输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
输出: 2
"""

#同leetcode216
#元素在数据集中出现的次数—>哈希表经常用到的功能！！！！
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        dict={}
        for num in nums:
            if num not in dict:
                dict[num]=1
            else:
                temp = dict.get(num)
                dict[num]=temp+1

        for key in dict.keys():
            if dict.get(key)>len(nums)//2:
                return key
        return 0
