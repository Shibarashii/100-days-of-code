import turtle
import random
from turtle import Turtle, Screen
import colorgram

turtle.colormode(255)
colors = colorgram.extract("image.jpg", 16)
rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

rgb_colors.remove((229, 228, 226))  # Removes the white (background)
rgb_colors.remove((225, 223, 224))  # Removes the white (background)

print(rgb_colors)

pagong = Turtle()
pagong.hideturtle()
pagong.penup()
pagong.goto(-255, -255)
pagong.speed("fastest")

for i in range(10):  # for loop for vertical movement
    for j in range(10):  # for loop for horizontal movement
        random_color = random.choice(rgb_colors)
        pagong.dot(20, random_color)
        pagong.forward(50)
    # After the horizontal movement ends,
    # Make the cursor go upwards and back to the start
    pagong.left(90)
    pagong.forward(50)
    pagong.setx(-255)
    pagong.right(90)


screen = Screen()
screen.exitonclick()
