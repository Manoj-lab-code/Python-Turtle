#Draw circle using python turtle with different fill colour


import turtle
Pen = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("red")
Pen.fillcolor("blue")
Pen.begin_fill()
Pen.circle(100)
Pen.end_fill()