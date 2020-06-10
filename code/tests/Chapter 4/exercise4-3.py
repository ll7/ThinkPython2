import turtle
import math

def draw_triangle(t, edge, length=50):
    
    t.fd(length)
    t.lt(180-edge)
    # cos = AK / HY -> AK = cos * HY
    AK = math.cos(edge*math.pi/180) * length
    t.fd(2*AK)
    t.lt(180-edge)
    t.fd(length)

def draw_pie(t, n_triangle, length):
    ang_tri_center = 360/n_triangle
    ang_tri_out = (180-ang_tri_center)/2
    
    for i in range (n_triangle):
        draw_triangle(t, ang_tri_out, length)
        t.lt(180)
    


def main():
    bob = turtle.Turtle()
    draw_pie(bob, 3, 100)
    turtle.mainloop()

if __name__ == '__main__':
    main()