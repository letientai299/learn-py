import turtle

wn = turtle.Screen()
wn.bgcolor('lightgreen')
wn.title('Tess and Alex')
wn.setup(600, 400)

tess = turtle.Turtle()
tess.color('hotpink')
tess.pensize(5)

alex = turtle.Turtle()
alex.pensize(3)

# make tess draw equilateral triangle
tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)

tess.right(180)
tess.forward(80)

# make alex draw a square
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)

wn.mainloop()
