import turtle

wn = turtle.Screen()

t = turtle.Turtle()
t.pensize(3)

for i in range(5):
    t.forward(200)
    t.left(180+180/5)

wn.mainloop()
