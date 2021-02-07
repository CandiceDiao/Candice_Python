"""
栈 常用操作
"""

##创建
##python用列表实现栈
stack =[]

##添加元素
##时间复杂度O(1)
stack.append(1)
stack.append(2)
stack.append(3)

##获取栈顶元素
##时间复杂度O(1)
#从后往前读
stack[-1]

##删除栈顶元素
##时间复杂度O(1)
#pop 删除最后一个元素并且！！！返回这个元素！！！
temp = stack.pop()

##栈的大小
##时间复杂度O(1)
len(stack)

##栈是否为空
##时间复杂度O(1)
len(stack)==0

##栈的遍历(边删除边遍历)
##时间复杂度O(N)
while len(stack)>0:
    temp = stack.pop()
