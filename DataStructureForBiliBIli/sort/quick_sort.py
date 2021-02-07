"""
快速排序(递归嵌套)： low, high, mid_value
最优时间复杂度：O(nlogn):每次都对半分
最坏时间复杂度：O（n^2）-->
稳定性：不稳定
"""

def quick_sort(alist,first,last):
    # n=len(alist)
    #列表只有一个元素时，排序终止
    if first >= last:
        return
    mid_value = alist[first]
    low = first
    high = last

    while low < high:
        # high左移
        # 把与mid_value相等的元素放到一边
        while low < high and alist[high] >= mid_value:
            # # 判断high
            # # 大于中间元素
            # # #该元素就应该留在右边，仅将high像左挪动1步
            # if alist[high] > mid_value:
            high -= 1
        alist[low] = alist[high]
        # low += 1
        # low右移
        while low < high and alist[low] > mid_value:
            low += 1
        alist[high] = alist[low]
        # high -= 1

    #从循环退出时，low=high
    alist[low] = mid_value

    # 需要在原来的list中进行修改，而不是切片以后的新list
    # quick_sort(alist[:low-1])
    # quick_sort(alist[low+1:])
    #对low左边的列表执行快速排序
    quick_sort(alist,first,low-1)
    # 对low右边的列表执行快速排序
    quick_sort(alist,low+1,last)


if __name__=='__main__':
    li=[24,23,93,17,77,31,44,55,20]
    print(li)
    li=quick_sort(li,0,len(li)-1)
    print(li)






