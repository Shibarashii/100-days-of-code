# instructions

# Write a program that interprets the Body Mass Index based
# on the user's weight and height.
#
# It should tell them the interpretation of their BMI
# based on their BMI value

# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.

# 🚨 Don't change the code below 👇

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

bmi = weight / height ** 2

if bmi <= 18.5:
    result = "Underweight"

elif bmi <= 25:
    result = "Normal"

elif bmi <= 30:
    result = "Slightly Overweight"

elif bmi <= 35:
    result = "Obese"

else:
    result = "Clinically Obese"


print(f"Your BMI is {bmi:.1f} and you are {result} ")


