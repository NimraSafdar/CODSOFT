import string
import random

def generate_password(length):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    all_characters = lowercase + uppercase + digits + symbols

    password = ''.join(random.choice(all_characters) for i in range(length))

    return password

    
try:
    length = int(input("Please specify the desired length of the password: "))
    if length < 4:
        print("Please choose a length greater than or equal to 4 for better security.")
       
        
    password = generate_password(length)
    print(f"Generated Password: {password}")

except ValueError:
        print("Please enter a valid number for the length.")

