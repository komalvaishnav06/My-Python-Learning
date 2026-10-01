# lists function
# 1) len/min/max/sorted
L = [2,1,5,7,0]
print('len(L): ',len(L))
print('min(L): ',min(L))
print('max(L): ',max(L))
print('sorted(L,reverse=True): ',sorted(L,reverse=True))

# 2) count
L = [1,2,1,3,4,1,5]
print('L.count(15): ',L.count(15))
print('L.count(5): ',L.count(5))

# 3) index
L = [1,2,1,3,4,1,5]
print("L.index(2): ",L.index(2))
print('L.index(1): ',L.index(1))

# 4) reverse
L = [2,1,5,7,0]
L.reverse()
print('L.reverse(): ',L)

# 5) sorted
L = [2,1,5,7,0]
print(L)
print('sorted (L): ',sorted (L))
print(L)
L.sort()
print('L.sort(): ',L)

# copy
L = [2,1,5,7,0]
print(L)
print(id(L))
L1 = L.copy
print(L1)
print(id(L1))