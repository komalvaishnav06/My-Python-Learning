#ques1) Find the length of a given string without using the len() function
# name = input("enter your name: ")
# counter = 0
# for i in name:
#     counter +=1
# print('length of the string is: ',counter)

#ques2) Extract username from a given email. 
# Eg if the email is nitish24singh@gmail.com 
# then the username should be nitish24singh
# email = input('enter your email: ')
# pos = email.index('@')
# print('the username is: ',email[0:pos])

#ques3) Count the frequency of a particular character in a provided string. 
# Eg 'hello how are you' is the string, the frequency of h in this string is 2.
# s = input("enter email: ")
# term = input('what would you like to search of: ')
# counter = 0
# for i in s:
#     if i == term:
#       counter +=1
# print('frequency of the character is: ',counter)

#ques4) Write a program which can remove a particular character from a string.
# s = input("enter your sentence: ")
# term = input('what would u like to remove: ')

# result = ''
# for i in s:
#    if i != term:
#       result = result + i
# print(result)

#ques5) Write a program that can check whether a given string is palindrome or not.
# abba
# malayalam
# k = input("enter word: ")
# flag = True
# for i in range(0,len(k)//2):
#    if k[i] != k[len(k) - i -1]:
#       flag = False
#       print('not a palindrome!')
#       break

# if flag:
#    print('palindrome')

#ques6) Write a python program to convert a string to title case without using the title()
# w = input('enter string: ')
# L = []
# for i in w.split():
#    L.append(i[0].upper() + i[1:].lower())
# print(" ".join(L))

#ques7) Write a program that can convert an integer to string.
number = int(input('enter number: '))

digits = '0123456789'
result = ''
while number != 0:
   result = digits[number % 10] + result
   number = number // 10
print(result)