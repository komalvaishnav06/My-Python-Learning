# operations on lists
# 1) arithmetic
L1 = [1,2,3,4]
L2 = [5,6,7]
print('L1+L2: ',L1+L2)
print('L1*9: ',L1*9)
# 2) membership
L1 = [1,2,3,4]
L2 = [1,2,3,[4,5]]
print(5 not in L1)
print(6 in L2)

# 3) loop
L1 = [1,2,3,4,5]
L2 = [1,2,3,4,[5,6]]
for i in L2:
    print(i)
for i in L1:
    print(i)

L1 = [1,2,3,4,5]
L2 = [1,2,3,4,[5,6]]
L3 = [[[1,2],[3,4]],[[5,6],[7,8]]]
for i in L3:
    print(i)
