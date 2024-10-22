#1
weather1=float(input('Enter the temperature of Monday'))
weather2=float(input('Enter the temperature of Tuesday'))
weather3=float(input('Enter the temperature of Wednesday'))
weather4=float(input('Enter the temperature of Thursday'))
weather5=float(input('Enter the temperature of Friday'))
weather6=float(input('Enter the temperature of Saturday'))
weather7=float(input('Enter the temperature of Sunday'))
Averagetemperature=(weather1+weather2+weather3+weather4+weather5+weather6+weather7)/7
print(Averagetemperature,'Celsius')
#2
x=float(input('Enter a number'))
y=float(input('Enter a second number'))
z=float(input('Enter a third number'))
pi=3.14
answer=(4*x**3)+(3*y**3)+(9*z)+(6*pi)
print(answer)
#3
time=input('Enter a number')
time=int(time)
minute=round(time//60)
second=time%60
print(minute,'minute', second,'seconds')
#4
hour=int(input('Enter an hour between 1 and 12'))
hoursahead=int(input('How many hours ahead you would like to know the time'))
theanswer=(hour+hoursahead)%12
print(theanswer)
#5
number = input("Enter a 3-digit number: ")
reversed_number = number[::-1]
print("Number reversed is:", reversed_number)
#6
month = int(input("Enter the Month: "))
day = int(input("Enter the Day: "))
day_of_year = (month - 1) * 30 + day
print(f"This is day {day_of_year} of the current year.")
