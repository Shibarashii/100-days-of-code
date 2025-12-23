# Instructor

# The objective is to take the inputs from the user to these
# questions and then generate a random password. Use your knowledge about
# Python lists and loops to complete the challenge.

# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

easy_password = ""
for i in range(nr_letters):
    easy_password += letters[random.randint(0, len(letters) - 1)]

for i in range(nr_symbols):
    easy_password += symbols[random.randint(0, len(symbols) - 1)]

for i in range(nr_numbers):
    easy_password += numbers[random.randint(0, len(numbers) - 1)]

print(easy_password)

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

random_list = []
hard_password = ""
for i in range(nr_letters):
    random_list.append(random.choice(letters))

for i in range(nr_symbols):
    random_list.append(random.choice(symbols))

for i in range(nr_numbers):
    random_list.append(random.choice(numbers))

for i in range(len(random_list)):
    random_value = random.choice(random_list)
    hard_password += random_value
    random_list.remove(random_value)

print(hard_password)

# SOLUTION FOR HARD LEVEL

# password_list = []
#
# for char in range(1, nr_letters + 1):
#   password_list.append(random.choice(letters))
#
# for char in range(1, nr_symbols + 1):
#   password_list += random.choice(symbols)
#
# for char in range(1, nr_numbers + 1):
#   password_list += random.choice(numbers)
#
# print(password_list)
# random.shuffle(password_list)
# print(password_list)
#
# password = ""
# for char in password_list:
#   password += char
#
# print(f"Your password is: {password}")
