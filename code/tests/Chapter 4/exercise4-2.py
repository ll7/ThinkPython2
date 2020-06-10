import turtle
import math

def draw_half_leave(t, leaves, length):
    for i in range(360//leaves):
            t.fd(length)
            t.lt(1)

def draw_flower(t, leaves=5, length=1):

    for l in range(leaves):
        draw_half_leave(t, leaves, length)

        t.lt(180-360//leaves)

        draw_half_leave(t, leaves, length)

        t.lt(180)

def main():
    print('start')

    bob = turtle.Turtle()

    draw_flower(bob, 7, 1)
    turtle.mainloop()

if __name__ == '__main__':
    main()