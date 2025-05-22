# Instructions

# Write a program that works out whether if a given year is a
# leap year

# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
leap_year = None
if year % 4 == 0:
    if year % 400 == 0:
        leap_year = True
    elif year % 100 == 0:
        leap_year = False
    else:
        leap_year = True
else:
    leap_year = False

if leap_year:
    print("That is a leap year")

else:
    print("That is not a leap year")