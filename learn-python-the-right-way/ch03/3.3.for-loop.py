import turtle

wn = turtle.Screen()

tess = turtle.Turtle()
tess.shape('turtle')
tess.color('blue')

tess.speed(15)
tess.penup()
size = 20

for i in range(120):
    tess.stamp()
    size = size+3
    tess.forward(size)
    tess.right(24)

wn.mainloop()
