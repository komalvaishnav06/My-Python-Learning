import sys

L = list(range(1000))
T = tuple(range(1000))
print('size of list: ',sys.getsizeof(L))
print('size of tuple: ',sys.getsizeof(T))