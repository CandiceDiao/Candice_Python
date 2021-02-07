"""
数组 常用操作
"""

# 创建数组：python中数组可以放任意类型；所以需要人为控制放入数组中的类型统一
l=[]

#添加元素
# 时间复杂度：O（1）在尾部添加
#            O（N） list尾部下一个存储空间被占用，需要重新为整个数组再找一块连续的存储空间
l.append(1)
l.append(2)
l.append(3)
print(l)

"""
插入元素
"""
#时间复杂度:O(N)
l.insert(2,99)

#访问元素
#时间复杂度:O(1) 用索引（下标）访问元素
temp = l[2]

#更新元素
#时间复杂度:O(1)
l[2]=88

"""
删除元素
"""
#1.直接删掉值
#时间复杂度:O(N) 需要从头到尾遍历找到该元素删除
l.remove(88)
#2.删除头元素
#时间复杂度:O(N) 删掉1位置元素，需要将后面元素往前移动
l.pop(1)
#3.删除最后一个元素
#时间复杂度:O(1) 删除最后一个元素，不需要移动其他元素位置
l.pop()
print(l)

"""
遍历数组3种方式
"""
#时间复杂度:O(N)
# 打印出元素位值
for i in l:
    print(i)

# 打印出元素位置+值
for index,element in enumerate(l):
    print(index,element)

# 打印出元素位置+值
for i in range(0,len(l)):
    print(i,l[i])

"""
查找某个元素的索引位置
"""
#时间复杂度:O(N) 返回值为2的索引 所以需要遍历列表，找到值为2的元素
index = l.index(2)

"""
排序
"""
#时间复杂度:O(NlogN)
l=[3,1,2]
#从小到大
l.sort()
#从大到小
l.sort(reverse=True)
