# editing items in list
L = [1,2,3,4,5]
L[-1] = 500
L[1] = 121
L[3:4] = 200,300
print(L)

# deleting items from list
L = [1,2,3,4,5]
# del L[-1]
del L[1:4]
print(L)

# remove
L = [1,2,3,4,5]
L.remove(3)
print(L)

# pop
L = [1,2,3,4,5]
L.pop(0)
print(L)

# clear
L = [1,2,3,4,5]
L.clear()
print(L)
