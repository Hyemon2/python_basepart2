import turtle
t =turtle.Turtle()
t.shape("turtle")
i=0
t.circle(30)
t.right(90)
while i<8:
    t.fd(100)
    j=0
    while j<3 :
        t.right(60)
        t.fd(50)
        t.right(180)
        t.fd(50)
        t.right(60)
        j+=1
    t.fd(100)
    t.right(90)
    t.circle(30)
    t.right(45)
    i+=1
    
