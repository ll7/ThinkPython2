import turtle

def draw_triangle(t, edge):
    for i in range(2):
        t.fd(50)
        t.lt(edge)
    t.fd(50)

def draw_pie(t, n_triangle):
    ang_tri_center = 360/n_triangle
    ang_tri_out = (180-ang_tri_center)/2
    
    draw_triangle(t, ang_tri_out)
    


def main():
    bob = turtle.Turtle()
    draw_pie(bob, 5)
    turtle.mainloop()

if __name__ == '__main__':
    main()