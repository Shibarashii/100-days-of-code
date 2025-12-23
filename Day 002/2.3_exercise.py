# Instructions

# Create a program using maths and f-Strings that tells us how many
# days, weeks, months we have left if we live until 90 years old

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

years = 90 - int(age)
months = years * 12
weeks = years * 52
days = years * 365

print(f"You have {days} days, {weeks} weeks, {months} months")
