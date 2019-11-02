import turtle as t

tree = t.Turtle()
tree.left(90)
tree.backward(100)
tree.speed(100)


def draw_tree(l):
    if l < 10:
        return
    else:
        tree.forward(l)
        tree.left(30)
        draw_tree(3*l / 5)
        tree.right(60)
        draw_tree(3*l / 4)
        tree.left(30)
        tree.backward(l)


draw_tree(100)

tree.getscreen()._root.mainloop()
