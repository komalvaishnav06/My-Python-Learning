# Dictionary
# Dictionary in Python is a collection of keys values, used to store data values like a map, which, unlike other data types which hold only a single value as an element.
# In some languages it is known as map or assosiative arrays.
# dict = { 'name' : 'nitish' , 'age' : 33 , 'gender' : 'male' }
# Characterstics:
# Mutable
# Indexing has no meaning
# keys can't be duplicated
# keys can't be mutable items
# dictionary are unordered


# I) Create Dictionary

# 1) empty dictionary
d = {}
print(d)
# 2) 1D dictionary
d1 = {'name':'komal','gender':'female'}
print(d1)
# 3) with mixed keys
d2 = {(1,2,3):4,'hello':'world'}
print(d2)
# 4)2D dictionary -> JSON
s = {
    'name':'dilkhush',
    'gender':'female',
    'age':41,
    'subjects':{
        'dsa':45,
        'c++':76,
        'dbms':98
    }
}
print(s)
# 5)using sequence and dict function
d3 = dict([('name','Himani'),('age',14),(3,3)])
print(d3)
# 6)duplicate keys
d4 = {'name':'komal','name':'phool'}
print(d4)
# 7)mutable items as keys
d5 = {'name':'komal',(1,2,3):2}
print(d5)