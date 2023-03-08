from turtle import *

s = Screen()
s.bgcolor('black')

t = Turtle()
t.pencolor('white')
t.width(3)
t.shape('turtle')

t.penup()

x = s.window_width() / 2
y = s.window_height() / 2

t.goto(-x + 10, +y - 10)

t.forward(100)
t.left(180)
t.pendown()
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)

t.penup()
t.forward(30)
t.pendown()

t.left(90)
t.forward(100)

t.penup()
t.right(90)
t.forward(130)
t.left(180)
t.pendown()

t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)

t.penup()
t.forward(30)
t.pendown()

t.left(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)

t.penup()
t.right(90)
t.forward(100)
t.right(90)
t.forward(50)
t.right(90)
t.pendown()
t.forward(100)

t.penup()
t.forward(30)
t.right(90)
t.forward(50)
t.right(90)
t.pendown()
t.write('❤', font=('Arial', 50))
t.penup()
t.right(90)
t.forward(45)
t.right(90)
t.forward(30)

done()