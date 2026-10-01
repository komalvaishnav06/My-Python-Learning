# Dictionary Operations

# Membership
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
print("'name' in s: ",'name' in s)
print("'dilkhush' in s: ",'dilkhush' in s)

# Iteration

d = {'name':'nitish','gender':'male','age':33}

for i in d:
    print(i,d[i])

