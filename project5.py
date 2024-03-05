# 集合的運算
s1={3,4,5}
print(3 in s1)
print(10 not in s1)

s1={3,4,5}
s2={4,5,6,7}
s3=s1&s2 # 交集: 取兩個集合中, 相同的資料
print(s3)
s3=s1|s2 # 聯集: 取兩個集合中的所有資料, 但不重複取用
print(s3)
s3=s1-s2 # 差集: 從 s1 中, 減去和 s2 重疊的部分
print(s3)
s3=s1^s2 # 反交集: 取兩個集合中, 不重疊的部分
print(s3)

s=set("hello") # 把字串中的字母拆解成集合: set(字串)
print("h" in s)

# 字典的運算: key-value 配對
dic={"apple":"蘋果","cat":"貓"}
print(dic["apple"])
print("apple" in dic) # 判斷 key 是否存在在字典中
del dic["apple"] # 刪除字典中的鍵值對 (key-value pair)
print(dic)
dic={x:x*2 for x in [3,4,5]}
print(dic)
