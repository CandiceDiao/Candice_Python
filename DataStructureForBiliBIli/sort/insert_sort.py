"""
插入排序:在已排序序列中从后向前扫描，找到相应位置并插入。
最优时间复杂度：O(n) （升序排列，序列已经处于升序状态）
最坏时间复杂度：O(n2)
稳定性：稳定
"""

def insert_sort(alist):
    n=len(alist)
    # 外层循环代表 从右边的无序序列中取出多少个元素执行这样的过程
    for j in range(1,n):
        #i 代表内层循环起始值
        i = j
        #内层循环代表执行从右边的无序序列中取出第一个元素，即i位置的元素，然后将其插入到前面的正确位置中
        while i > 0:
            #插入排序核心：后面元素与前面元素比较
            if alist[i] < alist[i-1]:
                alist[i], alist[i-1] = alist[i-1], alist[i]
                i -= 1
            else:
                break

    return alist

if __name__=='__main__':
    li=[24,23,93,17,77,31,44,55,20]
    print(li)
    li=insert_sort(li)
    print(li)

