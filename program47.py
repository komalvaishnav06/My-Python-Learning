# Sets
# creating sets
# 1) empty sets
s = set()
print (s)
print (type(s))

# 2) 1D and 2D sets
s1 = {1,2,3}
print('1D is: ',s1)
# s2 = {1,2,3,{4,5}}
# print(s2) y print nhi hoga kyonki y 2d form m h

# 3) homo and hetero
s3 = {1,'hello',4.5,True,(2,3,4)}  #true=1
print(s3)

# 4) using type conversions
s4 = set([1,2,3])
print(s4)

#  5) duplicates not allowed
s5 = {1,1,2,3,2,4,3}
print(s5)

# ques- 
s1={1,2,3}
s2={2,3,1}
print(s1 == s2)