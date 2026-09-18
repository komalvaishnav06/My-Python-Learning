# Find sum of 3-digit number entered by the user
number = int(input("enter a 3-digit number"))
a = number%10
number=number//10
b = number%10
number=number//10
c = number%10
print("the sum of 3-digit number is: ",a+b+c)