#1
for x in range(0,11,1):
    print(x)
#2
for x in range(10,-1,-1):
    print(x)
#3
for x in range(1,8):
    print('#' *x)

#4
rows=int(input('rows:'))
columns=int(input('columns:'))
for x in range(rows):
    for b in range(columns):
        print('#', end='')
    print()
#5
count=0
realcount=0
for x in range(0,11,1):
    count+=1
    multiply=x*(count-1)
    realcount=count-1
    print(x,'x',realcount,'=',multiply)
#6
for x in range(0,101,2):
    print(x)
#7
for x in range(2,101,2):
    minus=x-1
    print(minus)
    
#8
allnumber=0
for x in range(0,101,1):
    allnumber+=x
    print(allnumber)
#9
    allevennumber=0
for x in range(0,101,2):
    allevennumber+=x
    print(allevennumber)
 
alloddnumber=0
for b in range(2,101,2):
    minus=x-1
    alloddnumber+=minus
    print(alloddnumber)
    