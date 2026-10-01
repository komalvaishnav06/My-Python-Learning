a = int(input("enter first number: "))
b = int(input("enter second number: "))
c = int(input("enter third number: "))

if a<b and b<c:
    print("first is the smallest: ",a)
if b<a and b<c:
    print("second is smallest: ",b)
if c<a and c<b:
    print("third is smallest: ",c)