#071
sports = ['kickboxing,''Basketball,']
Favoritesport= input('What is your favorite sport:')
sports.append(Favoritesport)
sports.sort()
print('Sport list',sports)
#072
subjects = ['Construction', 'computer science', 'DCG',  'Maths', 'English', 'AG science']
print('subjects:' , subjects)
dislike = input('Wchich subjects you dont like?')
subjects.remove(dislike)
print('New subjects:' , subjects)
#074
color = ['blue', 'green', 'yellow', 'white', 'black', 'brown', 'red', 'pink', 'purple', 'gold']
start = int(input('Choose a number to start from 0 to 4:'))
end = int(input('Choose a number to end from 5 to 9:'))
print('Choose color:', color[start:end+1])
#075
numbers = ['123', '234', '345', '567']



