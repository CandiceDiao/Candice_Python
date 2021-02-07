"""no389 hash
给定两个字符串 s 和 t，它们只包含小写字母。

字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。

请找出在 t 中被添加的字母。
"""
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s)==0:
            return t
        #用数组创建一个大小为26的哈希表
        hastable = [0]*26
        for i in range(len(s)):
            #将字符转化成ASCII码-a的ASCII码
            temp = ord(s[i])-ord('a')
            #在s中出现的字符 哈希表中值-1
            hastable[temp] = hastable[temp]-1
        for j in range(len(t)):
            temp = ord(t[j])-ord('a')
            #s中如果是-1，t中为+1
            hastable[temp] = hastable[temp]+1
        for k in range(len(hastable)):
            if hastable[k] == 1:
                return chr(k+97)

s = Solution()
s.findTheDifference("abcd","abcde")


""""技巧一：使用ASCII码
技巧二：一减
        一加
        
1.数组实现hash表： 元素是确定的
将26个小写字母找到对应的ASCII码数字
{ key:ASCII码
  value：次数
2. 26个小写字母找到对应ASCII的数字
但是在数组中，不能创建那么大索引的数组。比如a-》97，创建索引为97的数组太大了
所以在数组中分别存放的是
a-a b-a c-a   的形式
  0  1     2
3. 一个数组解决的思路
s 里面每个元素出现的次数 -1
t 里面每个元素出现的次数+1
如果某一字符出现了相同次数，最后数组中的值为0
最后数组中值为1 的元素为多出来的元素 
4.最后得到元素的索引需要+97（a的ASCII码）
"""