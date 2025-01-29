word = 'house'
xy=list()
listword = list(word)
number = len(word)
blank = ' _ '*number
live = 7
position=0
print(blank)
while live >0 and '_' in blank :
     letter=input('Guess a letter:')
     print(live)
     if letter in listword and listword!='':
         print('correct')
         position+=word.find(letter)
         print(position)
         blank=blank[0:position]+letter+blank[position+1:]
         print(blank)
         position=1
     else:
         live-=1
         print('Wrong try again')
else:
    if live==0:
        print('You Lost!Game Over')
    else: 
        print('You Won! Game over')

     
   
    