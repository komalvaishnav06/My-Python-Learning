# lambda function

multi = lambda a,b: a*b
print(multi(2,4))

# lambda with map()
number = [1,2,3,4,5]
result = list(map(lambda x: x * x , number))

print(result)

# lamda with filter()
number = [1,2,3,4,5,6]
result = list(filter(lambda x: x % 2 == 0 , number))

print(result)