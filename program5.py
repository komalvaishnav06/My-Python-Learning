email=input("enter email: ")
password=input('enter password: ')

if email == 'komal@gmail.com' and password == '1234':
    print('welcome!')

elif email == 'komal@gmail.com' and password != '1234':
    print('password is incorrect')

    password = input('re-enter password')

    if password=='1234':
        print ("congratulations welcome!")
    else:
        print("beta tumse na ho payega")

else:
    print("incorrect account!")