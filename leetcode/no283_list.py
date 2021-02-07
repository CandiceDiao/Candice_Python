""" 283 数组
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。
"""
from typing import List


class Solution(object):
    def moveZeroes(self, nums:List):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 去除掉所有0元素
        index=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[index]=nums[i]
                index=index+1
        #将0元素不在数组后面
        for i in (index,range(len(nums))):
            nums[i]=0

"""
解题思路：
先遍历数组 将非零元素找到并填充到相应位置
然后再将后面补齐
"""