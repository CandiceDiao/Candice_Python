"""496 hash
用hash做法
"""
class Solution(object):
    def nextGreaterElement(self,nums1,nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        #返回数组
        res = []
        stack = []
        ht = {}

        for num in nums2:
            # 如果当前元素比栈顶元素大-》该值为栈顶元素的下一个最大值
            while(len(stack) !=0 and num>stack[-1]):
                #找到栈顶元素的下一个最大值，就需要将该元素弹出
                temp=stack.pop()
                #将栈顶元素 和下一个最大值加入到hash中
                ht[temp]=num
            #while走完以后说明num作为下一个最大值对应的key已经循环完毕
            #需要将num加入栈，为它寻找它的下一个最大值
            stack.append(num)
        # for 循环结束以后 hash 中包含的是nums2中一些元素的最大值
        # nums2后面有些元素可能还没有遍历到，还停留在栈中
        # 所以需要再次遍历一下栈
        while len(stack)!=0:
            #将栈中的元素取出作为key 保存到hash中 值为-1
            # 这些元素没有下一个最大值
            temp = stack.pop()
            ht[temp]=-1
        # 所有元素下一个最大值都在hash中
        for num in nums1:
            res.append(ht[num])
        return res







'''思路
hash中
key:存放 nums2中的每一个元素
value:存放num2中下一个最大的值

找num1元素的下一个最大的值
就是讲nums1中的元素去nums2中找对应key的value值

从后面到前面取值---》栈
'''