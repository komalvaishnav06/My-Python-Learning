# the current solution of a town 10000.the population of the town is increasing at the ate
#  of 10% per year. you have to write a program to find out the population at the end of each
#  of the last 10 years
current_pop = 10000
for i in range(10,0,-1):
    print(i,current_pop)
    current_pop = current_pop/1.1