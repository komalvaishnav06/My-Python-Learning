# swapping program without using 3rd variable
a = 1
b = 2
a,b = b,a
print('a=',a,'b=',b)

# other program
a,b,*others = (1,2,3,4)
print(a,b)
print(others)