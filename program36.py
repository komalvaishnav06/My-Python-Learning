# accessing items
# 1) indexing
t1 = (1,2,3,4,5)
t2 = (1,2,4,(6,4))
print(t1)
print(t1[2])
print(t2)
print(t2[-2])

# 2) slicing
print('slicing: ',t2[-1][0])
print('slicing: ',t2[-1])