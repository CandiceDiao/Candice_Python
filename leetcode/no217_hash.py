"""217 哈希 元组在数据集中出现的次数—>哈希表经常用到的功能！！！！
给定一个整数数组，判断是否存在重复元素。

如果存在一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)==0:
            return False
        dict ={}
        for num in nums:
            #如果从数组中取出的元素不在hash中，那么把他存入hash
            if num not in dict:
                dict[num]=1
            #如果元素存在于hash中，需要将原本hash该元素的value+1
            else:
                temp=dict.get(num)
                #统计元素出现次数
                dict[num]=temp+1
        #遍历hash中的值
        for key in dict.keys():
            if dict.get(key)>1:
                return True
        return False

"""
计算每个元素出现次数
hash{ key: 数组元素
      value: 元素出现次数
"""