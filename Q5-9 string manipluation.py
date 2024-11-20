#5
string = input ("Enter a string :")
length = len(string)
a = 0
end = length
string2 = ''
while a < length :
   if a == 0:
      string2 += string[0].upper()
      a += 1
   elif (string[a] ==''and string[a+1] !='') :
      string2 += string[a]
      string2 += string[a+1] .upper()
      a += 2
   else :
      string2 += string[a]
      a += 1
print ("Original String :", string)
print ("Capitalized words String", string2)
#6
word=input('Enter a word:')
length=len(word)
middle=len(word)
reverse=-1
for asd in range(middle):
    if word[asd]==word[reverse]:
        asd+=1
        reverse-=1
    else:
        print(word,'is not a palidrome')
        break
else:
    print(word,'is a palidrome')
#7
string = input("Enter a string:")
length = len(string)
maxlength = 0
maxsub = ''
sub = ''
lensub = 0
for a in range(length):
    if string[a] in 'aeiou' or string[a] in 'AEIOU':
        if lensub > maxlength:
            maxsub = sub
            maxlength = lensub
            sub = ''
            lensub = 0
    else:
        sub+= string[a]
        lensub= len(sub)
    a+=1
print("Maximum length consonant substring is:" , maxsub, end='')
print("with" ,maxlength,"characters")
#8
string = input('Enter a Word: ')
length = len(string)
print ('Origional string:',string)
string2 = ""
for a in range(0, length, 2) :
        string2 += string[a]
        if a < (length-1) :
            string2 += string[a+1]. upper()
print ('Alternative capitalized string:',string2)
#9   
email=input('Enter your email id:')
domain='@lwetb.ie'
ledo=len(domain)
lema=len(email)
sub=email[lema-ledo:]
if sub==domain:
  if ledo!=lema:
     print('It is valid email id')
  else:
     print('This is invalid email id - contains just the domain name.')
else:
     print('This email-id is either not valid or belongs to some other domain')
 