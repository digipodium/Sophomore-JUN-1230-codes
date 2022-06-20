from turtle import *

t = Turtle()
t.pensize(5)
bgcolor('green')
t.speed(0)
sides = 25
for i in range(sides):
    t.fd(30)
    t.lt(360/sides)
    t.circle(50)
    t.dot(20)
