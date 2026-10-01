lower = int(input("enter lower range: "))
upper = int(input("enter upper range: "))

for i in range(lower,upper+1):
    for j in range(2,i):
        if i%j == 0:
         break
    else:
       print(i)