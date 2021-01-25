# 如果a+b+c=1000 且a^2+b^2=c^2(a,b,c为自然数)，如何求出所有abc可能的组合？

import time
start_time = time.time()
# for a in range(0,1001):
#   for b in range(0,1001):
#      for c in range(0,1001):
#          #python中的幂运算a^2->a**2
#          if a+b+c==1000 and a**2+b**2==c**2:
#              print("a,b,c: %d,%d,%d"%(a,b,c))
'''
时间复杂度
T = 1000*1000*1000*2
T = 2000*2000*2000*2
n:解决问题的规模
T=  n*n*n*2
T(n) = n^3 * 2
T(n) = n^3 * 10

时间复杂度：T(n)
T(n) = k*g(n) k为系数，不改变函数走向，只影响陡峭
g(n) = n^3 g(n)是T(n)的一个渐进函数（忽略常数）
一个时间复杂度的大O表示法：O(g(n))

'''

#改进1：c=1000-a-b
for a in range(0,1001):
  for b in range(0,1001):
     c=1000-a-b
     if a**2+b**2==c**2:
         print("a,b,c: %d,%d,%d"%(a,b,c))

"""
T(n) = n * n * (1 + max(1,0))
T(n) = n^2 *2
     = O(n^2)
"""


end_time = time.time()
print("times:%d"%(end_time-start_time))
