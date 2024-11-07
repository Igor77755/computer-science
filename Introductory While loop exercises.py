#1
def average_integers_empty_string():
    total = 0
    count = 0
    while True:
        user_input = input("Enter an integer (or press Enter to stop): ")
        if user_input == "":
            break
        total += int(user_input)
        count += 1
    return total / count if count > 0 else 0
#2
def average_integers_negative():
    total = 0
    count = 0
    while True:
        user_input = int(input("Enter an integer (negative number to stop): "))
        if user_input < 0:
            break
        total += user_input
        count += 1
    return total / count if count > 0 else 0
#3
def average_grades():
    total = 0
    count = 0
    while True:
        user_input = int(input("Enter a test grade (negative number to stop): "))
        if user_input < 0:
            break
        total += user_input
        count += 1
    average = total / count if count > 0 else 0
    if average >= 90:
        letter_grade = 'A'
    elif average >= 80:
        letter_grade = 'B'
    elif average >= 70:
        letter_grade = 'C'
    elif average >= 60:
        letter_grade = 'D'
    else:
        letter_grade = 'F'
    return average, letter_grade
#4
def countdown_to_zero(n):
    for i in range(n, -1, -1):
        print(i)
#5
def even_numbers_up_to(n):
    for i in range(0, n + 1, 2):
        print(i)
has context menu 

