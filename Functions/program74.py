# paramters vs arguments
# type of arguments
# 1) default arguments
def power(a,b):
    return a**b
print('default arguments: ',power(2,3))
# 2) positional arguments
def power(a=1,b=1):
    return a**b
print('positional arguments: ',power(2,3))

# 3) keyword arguments
def power(a=1,b=1):
    return a**b
# power(b=2,a=3)
print('keyword arguments: ',power(b=2,a=3))