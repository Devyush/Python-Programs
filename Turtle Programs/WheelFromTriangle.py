import turtle
t=turtle.Turtle()
t.speed(0)
a=10
t.penup()
for j in range(1000):
    t.forward(a)
    t.left(120)
    t.pendown()
    t.forward(a)
    t.left(120)
    t.penup()
    t.forward(a)
    t.left(120)
    a=a+1
    t.left(5)
