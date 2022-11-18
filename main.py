from turtle import *
from random import *
import turtle
import time

setup(800, 500)
title("The Quickest, Slowest Turtle Race This Side of The Mississippi")
bgcolor("gray")
speed(4)

# Heading
penup()
goto(-100, 205)
color("black")
write("A Quick, Slow Turtle Race!", font=("Courier", 17, "bold"))

goto(-350, 200)
pendown()
color("black")
begin_fill
for i in range(2):
    forward(700)
    right(90)
    forward(400)
    right(90)
end_fill()

# finish line
gap_size = 20
shape("square")
penup()

# white squares row 1
color("white")
for i in range(10):
    goto(250, (170 - (i * gap_size * 2)))
    stamp()

# white squares row 2
for i in range(10):
    goto(250 + gap_size, ((210 - gap_size) - (i * gap_size * 2)))
    stamp()

# Purple squares row 1
color("black")
for i in range(10):
    goto(250, (190 - (i * gap_size * 2)))
    stamp()

# Black squares row 2
for i in range(10):
    goto(251 + gap_size, ((190 - gap_size) - (i * gap_size * 2)))
    stamp()

# First Racing Turtle - 
green_turtle = Turtle()
green_turtle.color("green")
green_turtle.shape("turtle")
green_turtle.shapesize(1.5)
green_turtle.penup()
green_turtle.goto(-300, 150)
green_turtle.pendown()

# Second Racing Turtle - 
turquoise_turtle = Turtle()
turquoise_turtle.color("turquoise")
turquoise_turtle.shape("turtle")
turquoise_turtle.shapesize(1.5)
turquoise_turtle.penup()
turquoise_turtle.goto(-300, -150)
turquoise_turtle.pendown()

# Third Racing Turtle - 
orange_turtle = Turtle()
orange_turtle.color("orange")
orange_turtle.shape("turtle")
orange_turtle.shapesize(1.5)
orange_turtle.penup()
orange_turtle.goto(-300, -50)
orange_turtle.pendown()


# Fourth Racing Turtle - 
brown_turtle = Turtle()
brown_turtle.color("brown")
brown_turtle.shape("turtle")
brown_turtle.shapesize(1.5)
brown_turtle.penup()
brown_turtle.goto(-300, 50)
brown_turtle.pendown()

# pause for 1 second before racing
start = turtle.Turtle()
style = ("Arial", 20, "bold")
start.hideturtle()
start.penup()
start.goto(-75, 0)
start.pendown()
start.color("black")
start.write("Ready, Set, Go! START", font=style)
time.sleep(2)
start.clear()

# move the turtles
while green_turtle.xcor() <= 230 and brown_turtle.xcor() <= 230 and orange_turtle.xcor() <= 230\
        and turquoise_turtle.xcor() <= 230:
    green_turtle.forward(randint(1, 10))
    brown_turtle.forward(randint(1, 10))
    orange_turtle.forward(randint(1, 10))
    turquoise_turtle.forward(randint(1, 10))

# celebrate the winner
winner = turtle.Turtle()
winner.hideturtle()
winner.penup()
winner.goto(-75, 0)
winner.pendown()
style = "Courier", 35, "italic", "bold"
if green_turtle.xcor() > brown_turtle.xcor() and green_turtle.xcor() > orange_turtle.xcor() and\
        green_turtle.xcor() > turquoise_turtle.xcor():
    winner.color("green")
    winner.write("Green Wins!", font=style)
elif brown_turtle.xcor() > green_turtle.xcor() and brown_turtle.xcor() > orange_turtle.xcor() and\
        brown_turtle.xcor() > turquoise_turtle.xcor():
    winner.color("brown")
    winner.write("Brown Wins!", font=style)
elif orange_turtle.xcor() > green_turtle.xcor() and orange_turtle.xcor() > brown_turtle.xcor() and\
        orange_turtle.xcor() > turquoise_turtle.xcor():
    winner.color("orange")
    winner.write("Orange Wins!", font=style)
else:
    winner.color("turquoise")
    winner.write("Turquoise Wins!", font=style)
time.sleep(3)
turtle.done()