from random import randint
from turtle import *

speed(0)


def flower():
    fillcolor("red")
    pencolor("orange")
    for i in range(5):
        lt(72)
        fd(80)
        circle(50)
        penup()
        bk(80)
        pendown()


for i in range(10):
    x = randint(-300, 300)
    y = randint(-300, 300)
    penup()
    goto(x, y)
    pendown()
    flower()
