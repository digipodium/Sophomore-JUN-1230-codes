HEIGHT = 500
WIDTH = 500

box1 = Rect((250, 200), (100, 10))
box2 = Rect((250, 0), (40, 40))
box3 = Rect((0, 200), (20, 20))
dbox2 = 10
dbox3 = 20

def draw():
    screen.fill("white")
    screen.draw.filled_rect(box1, "blue")
    screen.draw.filled_rect(box2, "green")
    screen.draw.rect(box3,'red')


def update():
    global dbox2  # telling the function that direction value we want to change
    global dbox3

    box2.y += dbox2
    box3.x += dbox3

    if box2.y > HEIGHT:
        box2.y = 0

    if box2.y < 0:
        box2.y = HEIGHT

    if box3.x > WIDTH:
        box3.x = 0

    if box3.x < 0:
        box3.x = WIDTH

    if box2.colliderect(box1):
        dbox2 = 20 if dbox2 == -20 else -dbox2
        sounds.hit.play()

    if box3.colliderect(box1):
        dbox3 = 10 if dbox3 == -10 else -dbox3
        sounds.hit.play()
