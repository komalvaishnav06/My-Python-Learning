fnum = int(input("enter num1: "))
snum = int(input("enter num2: "))

op = input ("enter the operation: ")

if op=='+':
    print('num1',fnum,'+',snum,'=',fnum+snum)
elif op == '-':
    print(fnum,'-',snum,fnum-snum)

elif op == '*':
    print(fnum,'*',snum,'=',fnum*snum)

elif op == '/':
    print(fnum,'/',snum,'=',fnum/snum)

else:
    print('invalid operation!')
