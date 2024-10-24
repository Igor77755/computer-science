#1
def calculate_days(x, y, z):
    return (x * y * z) / (x * y + y * z + x * z)
 
x = float(input("Enter days taken by A: "))
y = float(input("Enter days taken by B: "))
z = float(input("Enter days taken by C: "))
print("Days to complete work together:", calculate_days(x, y, z))
 
#2
a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b if b != 0 else "Cannot divide by zero")
 
#3
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
temp = a
a = b
b = temp
print("After swapping: a =", a, ", b =", b)
 
#4
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
a, b = b, a
print("After swapping: a =", a, ", b =", b)
 
#5
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
average = (a + b + c) / 3
print("Average:", average)
 
#6
import math
 
radii = [7, 12, 16]
for r in radii:
    volume = (4/3) * math.pi * (r ** 3)
    print(f"Volume of sphere with radius {r} cm:", volume)
 
#7
name = input("Enter your name: ")
age = int(input("Enter your age: "))
year_turn_100 = 2023 + (100 - age)
print(f"{name}, you will turn 100 years old in the year {year_turn_100}.")
 
#8
mass = float(input("Enter mass of the object (in kg): "))
c = 3 * 10**8  # speed of light in m/s
energy = mass * (c ** 2)
print("The energy of the object is:", energy, "Joules")