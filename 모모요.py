import turtle
t=turtle.Turtle()

def mycir(radius,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

    t.circle(radius)


mycir(100, 5, 5)
