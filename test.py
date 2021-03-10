# from ete3.test.test_treeview.seq_motif_faces import seq
# #
# dict = {'Google': 'www.google.com', 'Runoob': 'www.runoob.com', 'taobao': 'www.taobao.com'}
#
# print(type(dict.items()))
# print("字典值 : %s" % dict.items())
# 
# # 遍历字典列表
# for key, values in dict.items():
#     print(key, values)

# a=dict.fromkeys(1,("a","b","c"))
# print(a.items())
# dict={1:'a',2:"b",3:'c'}
# # print(dict.items())
# # for key,values in dict.items():
# #     print (key ,values)
# dict[3]='c'
# print(dict)
# s="abcd"
# print(dict(s))

# def xxx(c,d=1,*args,**kwargs):
#     print(c)
#     print(d)
#     print(args)
#     print(kwargs)
#     return(args[1])
#
# print(xxx(1,3,5,7,9,a=1,b=2))

#阶乘
def fact(n):
   if n==1:
       return 1
   else:
       return n*fact(n-1)

print(fact(5))

#幂的递归
def mi(a, n):
    if n == 0:
       return 1
    else:
       return a * mi(a, n - 1)

#遍历文件
import os
def get_file(path, rule=''):
    files = []
    for fpath, dirs, fs in os.walk(path):
        for f in fs:
            if os.path.join(fpath, f).endswith(rule):
                files.append(f)
    return files