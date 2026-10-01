# Editing key-value pair

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

s ['gender'] = 'male'
print(s)
s ['subjects']['dbms']= 76
print(s)