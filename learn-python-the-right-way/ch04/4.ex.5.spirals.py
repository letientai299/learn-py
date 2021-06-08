# this program doesn't print the exact output asked in the exercise,
# but I guess it's good enough.

import turtle

wn = turtle.Screen()
wn.bgcolor('lightgreen')

t = turtle.Turtle()
t.pensize(3)
t.speed(12)

turn_angle = 0
size = 5

for i in range(50):
    next_size = size + 10

    t.right(90)
    t.forward(size)

    t.right(90)
    t.forward(size)

    t.right(90)
    t.forward(next_size)
    t.right(90)
    t.forward(next_size)

    t.right(2)
    size = next_size + 10

wn.mainloop()
