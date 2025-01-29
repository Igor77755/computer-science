word = 'school'
xy=list()
listword = list(word)
number = len(word)
blank = ' _ '*number
live = 7
print(blank)
while live >0 and listword!=xy :
     letter=input('Guess a letter:')
     print(live)
     if letter in listword and listword!='':
         print('correct')
         x=list(letter)
         xy+=x
         print(xy)
     else:
         live-=1
         print('Wrong try again')
else:
    if live==0:
        print('You Lost!Game Over')
    else: 
        print('You Won! Game over')

     
   
    
    