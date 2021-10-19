import turtle
from turtle import Turtle , Screen
import random
turtle.colormode(255)
color_list = [(239, 236, 238), (238, 237, 236), (237, 237, 241), (26, 108, 164), (194, 38, 81), (237, 161, 50), (234, 215, 86), (226, 237, 229)]

tom = Turtle()
color = random.choice(color_list)
number_of_dots = 100
tom.penup()
tom.setheading(225)
tom.forward(250)
tom.setheading(0)
for dot_count in range(1, number_of_dots + 1):
    tom.penup()
    tom.dot(20, random.choice(color_list))
    tom.forward(30)
    if dot_count % 10 == 0:
        tom.setheading(90)
        tom.forward(30)
        tom.setheading(180)
        tom.forward(300)
        tom.setheading(0)
tom.hideturtle()

screen = Screen()
screen.exitonclick()