# Adding key-value pair

d1 = {'name':'komal','gender':'female'}
print(d1)
d1['name']='phool'
print(d1)

d3 = dict([('name','Himani'),('age',14),(3,3)])
print(d3)
d3['name']='dimple'
print(d3)

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
s['subjects']['maths']=34
print(s)