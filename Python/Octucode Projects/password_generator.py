import string
import random

print("Welcome to the Password Generator")

passowrd_length = int(input("Enter the number of characters in the password: "))

letters = int(input("Enter the number of letters in the password: "))
numbers = int(input("Enter the number of numbers in the password: "))
symbols = int(input("Enter the number of symbols in the password: "))

if (letters + numbers + symbols != passowrd_length):
    print("invalid input. The sum of letters, numbers, symbols doesn't match the password length try again")
else:
    ascii_letters = random.choices(string.ascii_letters, k=letters)
    digits = random.choices(string.digits, k=numbers)
    punctuation = random.choices(string.punctuation, k=symbols)
    
    # password_elements = []
    # password_elements.extend(ascii_letters)
    # password_elements.extend(digits)
    # password_elements.extend(punctuation)
    
    password_elements = ascii_letters + digits + punctuation
    
    random.shuffle(password_elements)
    
    separator  = ""
    password = separator.join(password_elements)
    separator.join(password)
    

    print(f"Genereted Passwod: {password}")



