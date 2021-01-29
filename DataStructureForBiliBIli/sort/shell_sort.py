"""
希尔排序：一种特殊的插入排序 gap（步长）
最坏时间复杂度：O（n^2）-->gap=1 插入排序
稳定性：不稳定
 """

def shell_sort(alist):
    n=len(alist)
    #n//2 两个斜线：取整数
    gap=n//2
    #gap变化到0之前，插入算法执行次数
    while gap>=1:
        #与普通的插入算法区别就是gap步长
        #交换操作从第一个gap 以后的序列跟前面序列进行比较交换
        #j=[gap,gap+1,gap+2]
        for j in range(gap,n):
            i=j
            # 从右到左比较 i=0时比较到左边第一个元素
            while i > 0:
                if alist[i] < alist[i - gap]:
                    alist[i], alist[i - 1] = alist[i - 1], alist[i]
                    i -= gap
                else:
                    break
        #缩短gap步长
        gap//=2



