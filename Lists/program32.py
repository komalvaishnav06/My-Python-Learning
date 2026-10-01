# list comprehension
# 1) add 1 to 10 numbers to a list
L = []
for i in range(1,11):
    L.append(i)
print(L)

L = [i for i in range (1,11)]
print(L)

# scalar multiplication on vector
v = [2,3,4]
s = -3
[-6,-9,-12]

print('[s*i for i in v]: ',[s*i for i in v])

# add squares
L = [1,2,3,4,5]
print('[i**2 for i in L]: ',[i**2 for i in L])