import turtle as tu

t = tu.Turtle()

t.left(90)
t.back(100)
t.clear()
t.wheel = 12
t.pensize(2)
t.pencolor("black")


def avance(l, n):
    if n == 0:
        t.forward(l)
    else:
        avance(l / 3, n - 1)
        t.left(90)
        avance(l / 3, n - 1)
        t.right(90)
        avance(l / 3, n - 1)
        t.right(90)
        avance(l / 3, n - 1)
        t.left(90)
        avance(l / 3, n - 1)


def curve(l, n):
    t.color('black', 'black')
    t.begin_fill()
    avance(l, n)
    t.left(90)
    avance(l, n)
    t.left(90)
    avance(l, n)
    t.left(90)
    avance(l, n)
    t.left(90)
    t.end_fill()
    t.hideturtle()


# main program
x = 300
t.speed(0)
curve(x, 3)

t.getscreen().mainloop()
