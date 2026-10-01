# Accessing items
my_dict = {'name':'jack','age':23}
# 1)[]
print(my_dict['name'])
# 2) get
print(my_dict.get('age'))

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
print(s['subjects'])
print(s['subjects']['c++'])