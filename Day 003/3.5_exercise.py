# Instructions

# Take both people's names and check for the number of
# times the letters in the word TRUE occurs. Then check for
# the number of times the letters in the word LOVE occurs. Then
# combine these numbers to make a 2-digit number.

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

combined_name = name1.lower() + name2.lower()

true = 0

true += combined_name.count("t")
true += combined_name.count("r")
true += combined_name.count("u")
true += combined_name.count("e")

love = 0

love += combined_name.count("l")
love += combined_name.count("o")
love += combined_name.count("v")
love += combined_name.count("e")

score = str(true) + str(love)

score = int(score)

if score < 10 or score > 90:
    message = "You go together like coke and mentos"

elif 40 < score < 50:
    message = "You are alright together"

else:
    message = ""

print(f"You score is {score}. {message}")
