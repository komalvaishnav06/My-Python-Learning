# kwargs
def display(**kwargs):
    for (key,value) in kwargs.items():
       print(key,'->',value)
    
print(display(india = 'delhi',punjab = 'chandigarh',rajasthan = 'jaipur',chattisgarh = 'raipur'))