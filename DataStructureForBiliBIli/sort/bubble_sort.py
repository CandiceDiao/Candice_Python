"""
冒泡排序:一次比较两个元素
最优时间复杂度：O（n）表示遍历一次发现没有任何可以交换的元素，排序结束
最坏时间复杂度：O(n^2)：内层循环+外层循环
稳定性：稳定
"""

def bubble_sort(alist):
    n=len(alist)
    #外层循环控制执行多少次，逐渐递增
    for j in range(0,n-1):
        count=0
        #内层循环控制从头走到尾
        for i in range(0,n-1-j):
            if alist[i]>alist[i+1]:
               alist[i],alist[i+1] = alist[i+1],alist[i]
            count+=1
        if count==0:
            #最优的情况，没有进行交换证明list本来就是有序的
            break
    return alist

#冒泡排序实现方式二：最外层循环方式逐渐减小
# def bubble_sort(alist):
#     for j in range(len(alist)-1,0,-1):
#         # j表示每次遍历需要比较的次数，是逐渐减小的
#         for i in range(j):
#             if alist[i] > alist[i+1]:
#                 alist[i], alist[i+1] = alist[i+1], alist[i]

def bubble_sort(alist):
    n = len(alist)
    for i in range(n):
        for j in range(0, n-i-1):
            if alist[j] > alist[j + 1]:
               alist[j], alist[j + 1] = alist[j + 1], alist[j]
    return alist


if __name__=='__main__':
    li=[24,23,93,17,77,31,44,55,20]
    print(li)
    li=bubble_sort(li)
    print(li)
