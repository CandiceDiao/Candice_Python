"""
队列 常用操作
"""

###创建队列
from collections import deque
# python中的deque创建的为一个双端队列
queue=deque()

##添加元素
#时间复杂度：O（1）
queue.append(1)
queue.append(2)
queue.append(3)

##获取元素：队头
#时间复杂度：O（1）
temp1=queue[0]

##删除即将出队的元素
#时间复杂度：O（1）
temp2 = queue.popleft()

##判断队列是否为空
#时间复杂度：O（1）
len(queue)==0

##遍历队列
#时间复杂度：O（N）
while len(queue)!=0:
    temp = queue.popleft()
    print(temp)
