import turtle


def draw_multicolor_square(t, sz):
    """
    Make turtle t draw a multi-color square of size sz
    """
    for c in ['red', 'purple', 'hotpink', 'blue']:
        t.color(c)
        t.forward(sz)
        t.left(90)


wn = turtle.Screen()
wn.bgcolor('lightgreen')

tess = turtle.Turtle()
tess.pensize(3)
size = 20

for i in range(15):
    draw_multicolor_square(tess, size)
    size = size+10
    tess.forward(10)
    tess.right(18)

wn.mainloop()
