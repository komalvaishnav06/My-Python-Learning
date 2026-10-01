# Remove key-value pair
d = {'name': 'nitish', 'age': 32, 3: 3, 'gender': 'male', 'weight': 72}
# pop
d.pop('gender')
print(d)

# popitem
d = {'name': 'nitish', 'age': 32, 3: 3, 'gender': 'male', 'weight': 72}
d.popitem()
d.popitem()
print(d) #popitem last item ko delete krta h

# del
d = {'name': 'nitish', 'age': 32, 3: 3, 'gender': 'male', 'weight': 72}
del d['name']
print(d)

# clear
d = {'name': 'nitish', 'age': 32, 3: 3, 'gender': 'male', 'weight': 72}
d.clear()
print(d)