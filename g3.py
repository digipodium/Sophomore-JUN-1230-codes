WIDTH = 500
HEIGHT = 500

box = Rect((30, 30), (50, 50))


def draw():
    screen.fill("white")
    screen.draw.filled_rect(box, "blue")


def update():
    print(box.x, box.y)
    box.x += 2
    if box.x > WIDTH:
        box.x = 0


# task
# 1. Increase the speed
# 2. Make the box move in different direction
# 3. Make two boxes with different color and move them
