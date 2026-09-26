import time
L = list(range(100000000))
T = tuple(range(100000000))

start = time.time()
for i in L:
    i*5
print('list time: ',time.time()-start)

start = time.time()
for i in T:
    i*5
print('tuple time: ',time.time()-start)