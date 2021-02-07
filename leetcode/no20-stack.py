"""20 stack
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。

"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #字符串为空
        if len(s) == 0:
            return True
        stack = []
        for w in s:
            if w in ('(', '{', '['):
                stack.append(w)
            else:
                if w in (')', '}', ']'):
                    #栈里面没有东西
                    if len(stack) ==0:
                        return False
                    #栈里面有东西
                    else:
                        temp = stack.pop()
                        if temp == "(" and w != ")":
                            return False
                        elif temp == "[" and w != "]":
                            return False
                        elif temp == "{" and w != "}":
                            return False
        #都遍历完成以后需要判断一下栈里还有没有左边的括号
        #{}( 这种情况
        if len(stack)==0:
            return True
        else:
            return False




if __name__=='__main__':
    s=Solution()
    print(s.isValid('[}'))