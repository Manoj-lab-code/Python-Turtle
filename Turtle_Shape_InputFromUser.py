#Write a program that makes your turtle draw shapes based on the input on the number of sides of #the shape.[Hint: keep the sides as 3,4,5, else skip]


import turtle
pen = turtle.Turtle()
screen = turtle.Screen()
numberofsides = int(input("enter number of sides of the shape"))
angle = 360/numberofsides
if numberofsides == 3:
  pen.forward(100)
  pen.left(angle)
  pen.forward(100)
  pen.left(angle)
  pen.forward(100)
  pen.left(angle)
elif numberofsides ==4:
  pen.forward(100)
  pen.left(angle)
  pen.forward(100)
  pen.left(angle)
  pen.forward(100)
  pen.left(angle)
  pen.forward(100)
  pen.left(angle)
elif numberofsides ==5:
  pen.forward(100)
  pen.left(angle)
  pen.forward(100)
  pen.left(angle)
  pen.forward(100)
  pen.left(angle)
  pen.forward(100)
  pen.left(angle)
  pen.forward(100)
  pen.left(angle)
else:
  pen.write("enter only 3, 4, 5")
screen.mainloop()

