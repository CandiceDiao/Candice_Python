"""
二分查找：有序序列
"""

#递归版本：每次传入一个新的列表
def binary_search(alist,item):
    n=len(alist)
    #递归调用退出条件
    if n>0:
        # 找到中间位置
        mid = n // 2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            return binary_search(alist[:mid], item)
        else:
            return binary_search(alist[mid + 1:], item)
    return False

if __name__=='__main__':
    li=[17,20,26,31,44,54,55,93]

    print(binary_search(li, 44))
    print(binary_search(li, 100))