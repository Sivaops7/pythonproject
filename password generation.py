#password generator
import random
letters = ['A', 'B', 'C',' D',' E', 'f', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['€', '$', '¢', '£', '¥']
numbers = ['0','1','2','3','4','5','6','7','8','9']
print("Welcome to the password Generation!")
nr_letter = int(input("How many letters would you like in your password \n"))
nr_symbols = int(input("How many symbols ould you like? \n"))
nr_numbers = int(input("how many numbers would you like? \n"))
password = []
for char in range(1,nr_letter+1):
    password += random.choice(letters)
for char in range(1,nr_symbols+1):
    password += random.choice(symbols)
for char in range(1,nr_numbers+1):
    password += random.choice(numbers)
random.shuffle(password)
print(password)
password1 = ""
for char in password:
    password1 += char
print(password1)


