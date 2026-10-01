# using if condition
products = {'phone':10,'laptop':0,'charger':32,'tablet':0}
print({key:values for (key,values) in products.items() if values>0})