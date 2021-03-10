"""
二分查找：操作对象必须为有序的，顺序表
时间复杂度 最优 O(1)
           最坏 O(logn)
"""

#递归版本：每次传入一个新的！！列表
def binary_search(alist,item):
    n=len(alist)
    #递归调用退出条件
    if n>0:
        # 找到中间位置
        # 不是在原有的列表上进行操作，每次都是新的列表。所以起点是0
        mid = n // 2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            # 递归版本：每次传入一个新的！！列表
            return binary_search(alist[:mid], item)
        else:
            # 递归版本：每次传入一个新的！！列表
            return binary_search(alist[mid + 1:], item)
    return False

if __name__=='__main__':
    li=[17,20,26,31,44,54,55,93]

    print(binary_search(li, 44))
    print(binary_search(li, 100))