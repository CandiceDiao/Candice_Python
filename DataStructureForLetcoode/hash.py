'''
哈希
'''

###创建
#用数组来创建，数组的索引当做哈希表的key
hashTable=['']*4
###用字典创建
mapping={}

###添加
#时间复杂度O（1）
#数组方式
hashTable[1]='haimeimei'
hashTable[2]='lihua'
hashTable[3]='siyang'
#字典
mapping[1]='haimeimei'
mapping[2]='lihua'
mapping[3]='siyang'

###修改
#时间复杂度O（1）
hashTable[1]='baishi'
mapping[1]='baishi'

###删除元素
#时间复杂度O（1）
hashTable[1]=''
mapping[1].pop()

###获取元素
#时间复杂度O（1）
hashTable[3]
mapping[3]

###检查key是否存在
#时间复杂度O（1）
#数组创建的哈希表，只能从头到为遍历一遍
#使用字典创建的哈希表：返回Ture/False
3 in mapping

##长度，是否含有元素
#时间复杂度O（1）
len(mapping)
len(mapping)==0