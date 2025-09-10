 How to make a different shape using python turtle with different fill color

# Import the turtle module
import turtle

# Create a turtle object and a screen object
pen = turtle.Turtle()
screen = turtle.Screen()

# Set the background color of the screen
screen.bgcolor("red")

# Set the fill color for the shape
pen.fillcolor("blue")

# Begin filling the shape
pen.begin_fill()

# Draw a circle with a radius of 100
pen.circle(100)

# End filling the shape
pen.end_fill()

# Keep the window open
turtle.mainloop()
