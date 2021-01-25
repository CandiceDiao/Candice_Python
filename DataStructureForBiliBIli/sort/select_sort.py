"""
选择排序:未排序序列中找到最小（大）元素
最优时间复杂度：O(n^2)
最坏时间复杂度：O(n^2)
稳定性：不稳定（考虑升序每次选择最大的情况）
"""
def select_sort(alist):
    n = len(alist)
    #最后一个元素肯定为最大值;所以n-1-》循环的数据范围0，n-2 倒数第二个元素即可
    for j in range(n-1):
        # 一开始从第一个数开始
        min_index = j
        for i in range(j+1, n):
            if alist[min_index] > alist[i]:
                min_index = i
        alist[j],alist[min_index] = alist[min_index],alist[j]
    return alist


if __name__=='__main__':
    li=[24,23,93,17,77,31,44,55,20]
    print(li)
    li=select_sort(li)
    print(li)





