# acessing items from list
# 1) positive indexing
L = [1,2,3,4,5]
print(L[2])
# 2) negative indexing
L = [1,2,3,[4,5]]
print(L[-1][-2])
# 3) slicing
L = [1,2,3,4,5]
print(L[0:3])
print(L[0::2])
print(L[-5:-2:-2])
print(L[::-1])