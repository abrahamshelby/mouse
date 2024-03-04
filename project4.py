# 有序可變動列表 List
# grades=[12,24,36,48,60]
# grades[1:4]=[] # 連續刪除列表中從編號 1 到編號 4(不包括) 的資料
# grades=grades+[72,84]
# length=len(grades) # 取得列表的長度 len (列表資料)
# print(length)
# print(grades[1:4]) # 取第一個數到第四個數(不包含四)
# grades[0]=55 # 把 55 放到列表中的第一個位置
# print(grades)
# data=[[3,4,5],[7,8,9]]
# print(data)
# data[0][0:2]=[5,5,5]
# print(data)
# 有序不可變動列表 Tuple
data=(3,4,5)
data[0]=5 # 錯誤: Tuple 的資料不可以變動
print(data)




