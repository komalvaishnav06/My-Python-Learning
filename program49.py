# deleting items
s = {1,2,3,4,5}
print(s)
# del s[0] indexing or slicing is not working
del s
s1 = {1,2,3,4,5,6}
s1.discard(3)
print('s1: ',s1)

s2 = {1,6,4,6,7,8,4}
s2.remove(4)
print("s2: ",s2)

s3 = {1,2,3,1,4,5}
s3.pop() #pop m random value delete hoti h
print('s3: ',s3)

s4 = {7,1,2,3,4}
s4.clear()
print('s4: ',s4)