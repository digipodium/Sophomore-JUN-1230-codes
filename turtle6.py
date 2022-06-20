from turtle import *
speed('fast')
side = 6
fillcolor('green')
pensize(5)
for i in range(side):
    fd(100)
    lt(360/side)
    begin_fill()
    circle(150)
    end_fill()

