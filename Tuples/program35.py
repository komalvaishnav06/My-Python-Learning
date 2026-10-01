# creating tuple
# empty
t1 = ()
print(t1)
# creating a tuple with a single item
t2 = ('hello',)
print(t2)
print(type(t2))
# homo
t3 = (1,2,3,4,5)
print(t3)
# hetero
t4 = (1,2,3,4,True,[1,2,7])
print(t4)
# tuple
t5 = (1,2,3,(4,5))
print(t5)
# using type conversion
t6 = tuple('hello')
print(t6)