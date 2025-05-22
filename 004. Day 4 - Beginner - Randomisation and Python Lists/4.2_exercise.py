# Instructions

# You are going to write a program which will select a random
# name from a list of names. The person selected will have to pay
# for everybody's food bill.
#
# Important: You are not allowed to use the choice() function.
#
#

import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

name_count = len(names)

random_person_paying_index = random.randint(0, name_count - 1)

print(f"{names[random_person_paying_index]} is going to buy the meal today")


