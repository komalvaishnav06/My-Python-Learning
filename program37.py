# operations on tuples
t1 = (1,2,3,4)
t2 = (5,6,7,(8,9))
# 1) arithmetic(+ and *)
print('a+b', t1 + t2)
print('a*2: ',t1*2 )

# 2) membership
print('2 in t1: ',2 in t1)
print('2 in t2: ',2 in t2)

# 3) iteration
for i in t2:
    print('loop: ',i)