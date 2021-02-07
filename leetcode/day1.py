from typing import List

# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for index, value in enumerate(nums):
            if target - value in cache:
                #返回符合条件的索引下标
                return [cache[target - value], index]
            cache[value] = index
        return None
# leetcode submit region end(Prohibit modification and deletion)

if __name__=='__main__':
    s=Solution()
    print(s.twoSum([3, 2, 4], 6))
