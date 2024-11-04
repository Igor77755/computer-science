#1
def triangle_type(a, b, c):
    if a == b == c:
        return "Equilateral"
    elif a != b and b != c and a != c:
        return "Scalene"
    else:
        return "Isosceles"
 
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
print(triangle_type(a, b, c))

#2
def check_last_digit(num):
    if num % 10 == 4:
        return "ends with 4"
    elif num % 10 == 8:
        return "ends with 8"
    else:
        return "ends with neither"
    
num =  int(input("Enter an integer:"))
print(check_last_digit(num))
#3
def print_numbers(N):
    for i in range(11, N + 1):
        if i % 3 == 0 and i % 7 == 0:
            print("Tipsy Topsy")
        elif i % 3 == 0:
            print("Tipsy")
        elif i % 7 == 0:
            print("Topsy")
        else:
            print(i)
 
N = int(input("Enter a number greater than 20: "))
if N > 20:
    print_numbers(N)
#4
def divisible_numbers(m, n):
    for i in range(1, m + 1):
        if i % n == 0:
            if i % 2 == 0:
                print(f"{i} is even")
            else:
                print(f"{i} is odd")
 
m = int(input("Enter m: "))
n = int(input("Enter n: "))
divisible_numbers(m, n)
 
#5
def sum_sequence(n):
    total = 0
    for i in range(1, n + 1):
        total += (2 * i)
    return total
 
n = int(input("Enter n: "))
print("Sum of the sequence:", sum_sequence(n))
#
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
 
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
 
temperature = float(input("Enter the temperature: "))
unit = input("Is this temperature in Celsius or Fahrenheit? ").strip().lower()
 
if unit == 'celsius':
    if temperature < -273.15:
        print("The temperature is invalid because it is below absolute zero.")
    elif temperature == 273.15:
        print("The temperature is absolute 0.")
    elif -273.15 < temperature < 0:
        print("The temperature is below freezing.")
    elif temperature == 0:
        print("The temperature is at the freezing point.")
    elif 0 < temperature < 100:
        print("The temperature is in the normal range.")
    elif temperature == 100:
        print("The temperature is at the boiling point.")
    else:
        print("The temperature is above the boiling point.")
    fahrenheit = celsius_to_fahrenheit(temperature)
    print(f"The temperature in Fahrenheit is: {fahrenheit:.2f}")
 
elif unit == 'fahrenheit':
    celsius = fahrenheit_to_celsius(temperature)
    print(f"The temperature in Celsius is: {celsius:.2f}")
else:
    print("Invalid unit. Please enter either 'Celsius' or 'Fahrenheit'.")
