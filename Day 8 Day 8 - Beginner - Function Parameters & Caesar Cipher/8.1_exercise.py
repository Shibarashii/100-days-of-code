# Instructions
import math
# You are painting a wall. The instructions on the paint can says
# that 1 can of paint can cover 5 square meters of wall. Given a
# random height and width of wall, calculate how many cans of paint
# you'll need to buy.

# Write your code below this line 👇


def paint_calc(height, width, cover):
    number_of_cans = math.ceil(height * width / cover)
    print(f"Number of cans needed: {number_of_cans}")

# Write your code above this line 👆

# Define a function called paint_calc() so that the code below works.

# 🚨 Don't change the code below 👇


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


