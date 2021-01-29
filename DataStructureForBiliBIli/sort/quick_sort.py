"""
快速排序： low, high, mid_value
最坏时间复杂度：O（n^2）-->gap=1 插入排序
稳定性：不稳定
"""

def quick_sort(alist):
    n=len(alist)
    mid_value = alist[0]
    low = 0
    high = n-1

    while low<high:
        # high左移
        while low < high and alist[high] > mid_value:
            # # 判断high
            # # 大于中间元素
            # # #该元素就应该留在右边，仅将high像左挪动1步
            # if alist[high] > mid_value:
            high -= 1
        alist[low] = alist[high]
        low += 1
        # low右移
        while low < high and alist[low] > mid_value:
            low += 1
        alist[high] = alist[low]
        high -= 1









