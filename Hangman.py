word = 'school'
blank=["_"]*len(word)
live=7
print(blank)
while live > 0 and "_" in blank:
    guess=input("Guess a letter:")
    if guess in word:
        for x, letter in enumerate(word):
            if letter==guess:
                blank[x]=guess
    else:
         live-=1
         print('Wrong try again')
         print('You lost a life')
    print(blank)
else:
    if live==0:
        print('You lost!Game Over')
    else:
        print('You Won!Game Over')
        