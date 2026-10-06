def is_even(num):

    """this function is return if a given number is odd or even 
    input - any valid integer
    output - even/odd   
    created on 16th nov 2022"""
    if type(num) == int:
        if num % 2 == 0:
         return 'even'
        else:
         return 'odd'
    else:
        return 'pagal hai kya?'
for i in range(1,11):
    x = is_even(i)
    print(x)

is_even('hello')