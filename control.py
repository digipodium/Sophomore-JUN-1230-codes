HEIGHT = 300
WIDTH = 600

player = Actor('alien',(50,50))
bg = Actor('background')

def draw():
    bg.draw()
    player.draw()

def update():
    if keyboard.left:
        player.x += -3
    if keyboard.right:
        player.x += 3
    if keyboard.up:
        player.y += -3
    if keyboard.down:
        player.y += 3



