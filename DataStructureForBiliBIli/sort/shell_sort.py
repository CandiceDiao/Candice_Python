"""
希尔排序：一种特殊的插入排序
"""

def shell_sort(alist):
    n=len(alist)
    #n//2 两个斜线：取整数
    gap=n//2
    i = 1
    if alist[i]<alist[i-1]:
        alist[i],alist[i-1]=alist[i-1],alist[i]
    else:
        break

