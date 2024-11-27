#1
import re
def validate_phone_number():
    phone_number = input("Enter a phone number (format: xxx-xxx-xxxx): ")
    pattern = r'^\d{3}-\d{3}-\d{4}$'
    if re.match(pattern, phone_number):
        print("The phone number format is valid.")
    else:
        print("The phone number format is invalid.")
 
validate_phone_number()

#2
def extract_and_sum_digits():
    user_input = input("Enter a string: ")
    digits = re.findall(r'\d', user_input)
    if digits:
        digit_sum = sum(int(d) for d in digits)
        print(f"{user_input} has the digits {''.join(digits)} which sum to {digit_sum}")
    else:
        print(f"{user_input} has no digits")
        
extract_and_sum_digits()

#3
sentence = input("Please type a sentence(s): ")


words = sentence.split()
num_words = len(words)


num_chars = len(sentence)

num_alnum = sum(c.isalnum() for c in sentence)
percentage_alnum = (num_alnum / num_chars) * 100 if num_chars > 0 else 0

print("\nOriginal sentence(s):", sentence)
print("Number of words:", num_words)
print("Number of characters:", num_chars)
print(f"Percentage of alphanumeric characters: {percentage_alnum:.2f}%")
#4
def main():
    while True:
        sentence = input("Please enter a sentence, or 'q' to quit: ")

        if sentence.lower() == 'q':
            break
        transformed_sentence = sentence.lower()

        print(transformed_sentence)

main()
#5
def extract_and_add():
    integer_input = int(input("Enter an integer: "))
    string_input = input("Enter a string: ")

    extracted_digits = ''.join([char for char in string_input if char.isdigit()])

    if not extracted_digits:
        extracted_digits = '0'

    extracted_digits_int = int(extracted_digits)

    result_sum = integer_input + extracted_digits_int

    print(f"{integer_input} + {extracted_digits} = {result_sum}")

extract_and_add()
#6
def compare_strings(str1, str2):
    if str1 < str2:
        smaller, larger = str1, str2
    else:
        smaller, larger = str2, str1

    print(f"Smaller string: {smaller}")
    
    print("Larger string in the format:")
    length = len(larger)
    
    for i in range((length + 1) // 2):
        print(f"{larger[i]} {larger[length - i - 1]}")

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

compare_strings(string1, string2)
#7
def int_to_roman(num):
    roman_numerals = [
        ('M', 1000),
        ('CM', 900),
        ('D', 500),
        ('CD', 400),
        ('C', 100),
        ('XC', 90),
        ('L', 50),
        ('XL', 40),
        ('X', 10),
        ('IX', 9),
        ('V', 5),
        ('IV', 4),
        ('I', 1)
    ]
    
    roman_string = ""
    
    for roman, value in roman_numerals:
        while num >= value:
            roman_string += roman  
            num -= value 
            
    return roman_string

number = int(input("Enter a number: "))
roman_numeral = int_to_roman(number)
print(f"The Roman numeral for {number} is: {roman_numeral}")


