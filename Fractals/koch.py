import turtle as tu

t = tu.Turtle()

t.speed(10)
t.backward(100)
t.right(90)
t.backward(100)
t.left(90)
t.clear()


def koch(length, depth):
    if depth == 0:
        t.forward(length)
    else:
        koch(length/3, depth-1)
        t.left(60)
        koch(length/3, depth-1)
        t.right(120)
        koch(length/3, depth-1)
        t.left(60)
        koch(length/3, depth-1)


for i in range(3):
    koch(200, 2)
    t.right(120)

t.getscreen().mainloop()
