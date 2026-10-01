# using existing dict
distances = {'delhi':1000,'mumbai':2000,'bangalore':3000}
print(distances.items())

distances = {'delhi':1000,'mumbai':2000,'bangalore':3000}
print({key:values*0.62 for (key,values) in distances.items()})