import turtle

wn = turtle.Screen()

t = turtle.Turtle()
t.pensize(5)
t.shape('turtle')

# draw the center of the clock
t.stamp()

t.penup()

for i in range(12):
    t.forward(200)
    # draw the short straigh line
    t.pendown()
    t.forward(30)
    t.penup()
    t.forward(20)

    # draw the short straigh line
    t.stamp()

    # go back to center
    t.backward(250)

    # prepare for the next hour
    t.right(360/12)

wn.mainloop()
