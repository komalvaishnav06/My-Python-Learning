s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}

# 1) union(|)
print('1) union(|): ',s1 | s2)
# 2) intersaction(-)
print('2) intersaction(-): ',s1 - s2, ' and ',s2 - s1 )

# 3) symmetric difference(^)
print('3) symmetric difference(^): ', s1 ^ s2)

# 4) membership test
print('4) membership test: ',1 not in s1)

# 5) iteration
for i in s1:
    print('5) iteration: ',i)