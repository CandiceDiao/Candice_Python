"""
归并排序(递归！！！嵌套)： 拆分 排序后得到一个!!!新的列表!!!
最优时间复杂度：O(nlongn)
最坏时间复杂度：O(nlongn)
稳定性：稳定
"""

def merge_sort(alist):

    n=len(alist)
    #拆分到都只剩下一个元素，拆分停止
    if n<=1:
        # 拆分结束后，alist中只剩下一个元素，将alist return 即可
        return alist
    # 拆分
    mid = n//2
    #left 采用归并排序后形成的有序的新的列表
    left_li = merge_sort(alist[:mid])
    #right 采用归并排序后形成的有序的新列表
    right_li = merge_sort(alist[mid:])

    #合并:将两个有序的子序列合并为一个新的整体
    #merge(left,right)
    #定义两个游标
    left_pointer,right_pointer =0,0
    #result 用于存放合并后的新列表
    result=[]
    while left_pointer<len(left_li) and right_pointer<len(right_li):
        if left_li[left_pointer] <= right_li[right_pointer]:
            # 把小的值添加到新列表中
            result.append(left_li[left_pointer])
            # 左指针像右移动
            left_pointer += 1
        else:
            result.append(right_li[right_pointer])
            right_pointer += 1
    #退出while循环后；将列表剩下的部分追加到新的列表中？
    result +=left_li[left_pointer:]
    result += right_li[right_pointer:]
    return result

if __name__=="__main__":
    li=[24,23,93,17,77,31,44,55,20]
    print(li)
    sorted_li = merge_sort(li)
    #归并排序后原列表没有被修改
    print(li)
    #排序后的新列表
    print(sorted_li)

'''
##########函数执行过程##########
li=[54,23,93,17,77,31,44,55,20]

#####左边部分执行过程
left_li = merge_sort[54,26,93,17]
         
         left_li = merge_sort[54,26]
                   #拆分到最后一个元素
                    left_li=[54]
                    #递归调用，往上一层找merge_sort[54,26]
                    right_li=[26]
                    #进行合并
                    result = [26,54]
                    return result
        ->left_li = [26,54]
        right_li = merge_sort([93,17])
                   left_li = merge_sort([93])
                           reutrn 93
                    ->left_li = 93
                   right_li = merge_sort([17])
                            return 17
                   ->right_li=17
                   #进行合并
                   result = [17,93]
                   return result
        ->right_li=[17,93]
        #合并
        result =[17,26,54,93]
        ->retrun result
*left_li=[17,26,54,93]

###右边执行过程
right_li=merge_sort([77,31,44,55,20])   
 ...
 ...
 *right_li = [20,31,44,55,77]
 
###最后合并  *left_li  *right_li  
'''




