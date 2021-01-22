# CMPT 120
# Turtle Artist
# Author: Henry Yin
# Section: D200

# Defined Functions

# 1. draw a square of a fixed value
def square_side100():
    for i in range(4):
        t.forward(100)
        t.left(90)
    return

# 2. draw a square with a side value based on parameter
def squareValue(side):
    for i in range(4):
        t.forward(side)
        t.left(90)
    return

# 3. clears and sends turtle back to original position
def startAgain():
    t.penup()
    t.home()
    t.pendown()
    t.clear()
    return

# 4. returns a color
def randomColor():
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random. randint(0,255)
    colorToReturn = (red,green,blue)
    return colorToReturn

# 5. draws square side size filled with color
def square_with_color(side,color):
    t.fillcolor(color)
    t.begin_fill()
    squareValue(side)
    t.end_fill()
    return

# 6. moving the pen forward 200
def movingpen():
    t.penup()
    t.forward(200)
    t.pendown()
    return

# 7. draws circle filled with color
def circle_with_color(radius,color):
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    return

# 8. draw a part of spiral with color
def spiral_part(side,color):
    for i in range(2):
        t.color(color)
        t.forward(side)
        t.left(90)
    return

##################################################
# Top level 

import turtle as t
import random 

# Square Art
square_side100()

startAgain()

square_side=int(input("What size of the square side?-->"))
squareValue(square_side)

movingpen()

pen_color=input("What color of the pen?-->")
square_color=input("What color filling the square?-->")
t.pencolor(pen_color)
square_with_color(square_side,square_color)

startAgain()

# LabWk5 10b
# 1.
t.pensize(5)
t.color("blue")
t.fillcolor("lightgreen")
t.begin_fill()
t.circle(50)
t.end_fill()

movingpen()

# 2.
t.color("red")
square_side100()

movingpen()

#3.
t.pencolor("black")
t.forward(100)
t.left(90)
t.forward(50)
t.right(90)
t.forward(100)
t.backward(100)
t.left(90)
t.forward(50)
t.right(90)
t.forward(100)

startAgain()

# LabWk6 15
# 1.
for i in range(50,200,50):
    squareValue(i)

startAgain()

# 2.
t.colormode(255)
for i in range(150,0,-50):
    col=randomColor()
    circle_with_color(i,col)

startAgain()

# LabWk6 16
for i in range(20,200,20):
    col=randomColor()
    spiral_part(i,col)

startAgain()

# turtle shape
t.shape("turtle")
t.penup()
for i in range(5):
    for i in range(15):
        t.forward(20)
        t.stamp()
    t.right(144)

startAgain()

#
t.pencolor("violet")
wn= t.Screen()
wn.bgcolor("lightgreen")
for i in range(3,10):
    for a in range(i):
        t.forward(100)
        angle=360/i
        t.left(angle)
    for a in range(i):
        t.forward(100)
        t.right(angle)

    

    


