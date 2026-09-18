import random
jackpot = random.randint(1,100)
guess = int(input("guess karo"))
counter = 1
while guess != jackpot:
    if guess<jackpot:
        print('galat!guess higher')
    else:
        print('galat guess lower')

    guess = int(input('guess karo'))
    counter +=1

else:
     print('correct guess')
     print('attempts',counter)