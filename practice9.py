# 2.1 The split() Method

text = 'i love phool'
print(text.split())

a = input('enter sentence: ')
print(a.split())

# by using seperator
b = 'According to adam smith'
print(b.split("/"))

# by using maxsplit
c = 'i love phool she is cute'
print(c.split(" ",1))
print(c.split(" ",2))
print(c.split(" ",3))