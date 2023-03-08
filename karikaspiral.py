from turtle import *

s = Screen()
s.bgcolor('black')

t = Turtle()
t.width(2)
t.shape('turtle')
t.speed('fastest')
t.color('white')

colors = ['red', 'green', 'blue', 'orange', 'yellow', 'purple']

for x in range(100):
    t.pencolor(colors[x%6])
    t.penup()
    t.forward(x*2)
    t.pendown()
    t.circle(int(x/4) + 1)
    t.left(58)

t.penup()
t.left(58)
t.goto(0, 0)

done()
